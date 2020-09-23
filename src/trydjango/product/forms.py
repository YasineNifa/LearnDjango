from django import forms

from .models import Product


# 2 diffrent way to handle forms
#First
class ProductForm(forms.ModelForm):
	title		= forms.CharField(label='Product',widget = forms.TextInput(attrs={"placeholder":"Your title"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"New Description", "class":"new-class-name two","rows":3,"cols":60}))
	price 		= forms.DecimalField(initial=0)
	email 		= forms.EmailField()
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]


	# VALIDATION Examples
	def clean_title(self, *args,**kwargs):
		title = self.cleaned_data.get("title")
		if not "Prod" in title:
			raise forms.ValidationError("This is not a valid title")
		return title

	def clean_email(self, *args,**kwargs):
		email = self.cleaned_data.get("email")
		if not "@" in email:
			raise forms.ValidationError("This is not a valid email")
		return email

#Second
# Now we will add some widget
class RawProductForm(forms.Form):
	#By default required is True
	title		= forms.CharField(label='Product',widget = forms.TextInput(attrs={"placeholder":"Your title"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"New Description", "class":"new-class-name two","rows":3,"cols":60}))
	price 		= forms.DecimalField(initial=0)