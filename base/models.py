from django.contrib.auth.models import User
from django.db import models

# Create your models here.
##create user model parameter

USER_ROLE = (('Owner','Owner'),('Employee','Employee'))

MENU_NAME = (
    ('Breakfast','Breakfast'),
    ('Lunch','Lunch'),
    ('Snacks','Snacks'),
    ('Dinner','Dinner')
    )

class Employees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)
    user_role = models.CharField(choices=USER_ROLE,max_length=12,default=None)
    image = models.ImageField(null=True,default="avatar.svg",upload_to='emp_pic')
    def __str__(self):
        return self.name


# Restaurant:
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    phone = models.IntegerField(default = 0)
    owner_id = models.ForeignKey(Employees,on_delete= models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()



# Menu:
class Menu(models.Model):
    menu_name = models.CharField(choices = MENU_NAME,max_length=20)
    restaurant_name = models.ForeignKey(Restaurant, on_delete = models.CASCADE )

    def __str__(self):
        return self.menu_name

# Item:
class Item(models.Model):
    menu_ref = models.ForeignKey(Menu,on_delete = models.CASCADE)
    item_name = models.CharField(max_length = 100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    item_image = models.ImageField(upload_to='item_image')

    def __str__(self):
        return self.item_name

# Cart:
class Cart(models.Model):
    user = models.ForeignKey(Employees, on_delete = models.CASCADE)
    product_item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    @property
    def total_cost(self):
        return self.quantity * self.product_item.discount_price

# Payment:
class Payment(models.Model):
    user = models.ForeignKey(Employees, on_delete = models.CASCADE)
    rastaurant_name = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add = True)
    paid = models.BooleanField(default = False)

#Order Placeed 
STATUS_CHOICES = {
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending')
}    

class OrderPlaced(models.Model):
    user = models.ForeignKey(Employees, on_delete=models.CASCADE)
    product_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")

    @property
    def total_cost(self):
        return self.quantity * self.product_item.discount_price