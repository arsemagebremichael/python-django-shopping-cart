

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem
from django.views.decorators.http import require_POST


from django.contrib.auth.decorators import login_required
from .forms import ProductForm
def list_products(request):
    products = Product.objects.all()
    return render(request, "catalogue/products.html", {"products": products})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "catalogue/product_details.html", {"product": product})

@require_POST
def add_to_cart(request, id):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    product = get_object_or_404(Product, pk=id)
    cart_item, created = CartItem.objects.get_or_create(product=product, session_key=session_key)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('list_products')


@login_required
def cart_detail(request):
    print('User authenticated:', request.user.is_authenticated)
    print('Session key:', request.session.session_key)
    session_key = request.session.session_key
    if not session_key:
        cart_items = []
        total = 0
    else:
        cart_items = CartItem.objects.filter(session_key=session_key)
        total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'catalogue/cart_detail.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, id):
    session_key = request.session.session_key
    if session_key:
        cart_item = get_object_or_404(CartItem, pk=id, session_key=session_key)
        cart_item.delete()
    return redirect('cart_detail')


@login_required
def product_upload(request):
    if request.method == 'POST':
        form = ProductForm

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()
    return render(request, 'catalogue/product_upload.html', {'form': form})

