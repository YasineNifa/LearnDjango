from django import forms

from .models import Product


# 2 diffrent way to handle forms
#First
class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

#Second
# Now we will add some widget
class RawProductForm(forms.Form):
	#By default required is True
	title		= forms.CharField(label='Product',widget = forms.TextInput(attrs={"placeholder":"Your title"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"New Description", "class":"new-class-name two","rows":3,"cols":60}))
	price 		= forms.DecimalField(initial=0)