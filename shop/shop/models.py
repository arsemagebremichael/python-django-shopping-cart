from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=28)
class Tag (models.Model):
   name = models.CharField(max_length=28)
class Subscription(models.Model):
    name = models.CharField(max_length=50)
class Product (models.Model):
    name = models.CharField(max_length=50)
    Category= models.ForeignKey(Category,null=True, on_delete=models.PROTECT)
    tags=models.ManyToManyField(Tag,blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    def __str__(self):
        return f"{self.name}, price {self.price}"