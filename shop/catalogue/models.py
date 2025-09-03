from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=28)


class Tag (models.Model):
   name = models.CharField(max_length=28)


class Subscription(models.Model):
    name = models.CharField(max_length=50)


class Product (models.Model):
    name = models.CharField(max_length=50)
    category= models.ForeignKey(Category,null=True, on_delete=models.PROTECT)
    tags=models.ManyToManyField(Tag,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    def __str__(self):
        return f"{self.name}, price {self.price}"
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    session_key = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"