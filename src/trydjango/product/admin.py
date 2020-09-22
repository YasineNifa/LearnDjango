from django.contrib import admin
from .models import Product
# Register your models here.

# To save a table names Product in our database
admin.site.register(Product)
#Go to the admin page and add new entries for this table