from django.db import models

# Create your models here.
# store a product, I want my backend to have a memory of a product that I created
# HOW?
# I want that to map to our database, how can I do that ?
class Product(models.Model):
	title 		= models.CharField(max_length=100)
	description = models.TextField(blank=True)#or null=True
	price 		= models.DecimalField(decimal_places=2, max_digits=10000)
	summary		= models.TextField()
	Featured	= models.BooleanField(default=True)
# After creatin g a model I have to execute
# python manage.py makemigrations
# python manage.py migrate

# if for example we add a new field to our model, and we had alredy
# created some entries in our Product table, we will be getting
# an error because we django son't know what to put 
# in this field for the previous entries
# To solve it you can add a default parameter for the new fields
# or use the null paramaetr as True 

# blank has to do how the field is render
# null with the database
# blank = False means it is required
