
from django.urls import path
from . import views  


urlpatterns = [
    path("products/", views.list_products, name="list_products"),
    path("products/<int:id>/", views.product_detail, name="product_details"),
    path("add-to-cart/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("remove-from-cart/<int:id>/", views.remove_from_cart, name="remove_from_cart"),
    path('product/upload/', views.product_upload, name='product_upload'),
]
