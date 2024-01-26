from django.contrib import admin

from .models import Cart
from .models import Employees
from .models import Item
from .models import Menu
from .models import OrderPlaced
from .models import Payment
from .models import Restaurant

# Register your models here.

admin.site.register(Employees)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(OrderPlaced)
