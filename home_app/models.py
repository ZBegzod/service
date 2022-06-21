import datetime
from django.db import models
from django.contrib.auth.models import User

class Combo(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self) -> str:
        return self.name
   
class Resurs(models.Model):
    name = models.CharField(max_length=75)
    product_quantity = models.IntegerField()
    price = models.FloatField()
    products = models.ManyToManyField(Combo, through = 'Product')

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    resurs = models.ForeignKey(Resurs, on_delete=models.CASCADE)
    product_size = models.FloatField()
    
    def __str__(self) -> str:
        return f"{self.combo} {self.resurs}"

class Fast_food_branch(models.Model):
    name = models.CharField(max_length=75)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} {self.rating}"

class Orders(models.Model):
    fast_food_branch_id = models.ForeignKey(Fast_food_branch, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=datetime.datetime.today)
    
    def __str__(self) -> str:
        return self.date_time
    
class Order_client(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    combo = models.ForeignKey(Combo, on_delete=models.DO_NOTHING)
    resurs = models.ForeignKey(Resurs, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    fast_food = models.ForeignKey(Fast_food_branch, on_delete=models.DO_NOTHING)
    orders = models.ForeignKey(Orders, on_delete=models.DO_NOTHING)

