from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

from .forms import ProductForm, RawProductForm

# Create your views here.

def product_detail_view(request, *args,**kwargs):
	obj = Product.objects.get(id=1)
	# context = {
	# 	'title':obj.title,
	# 	'price':obj.price,

	# }
	context = {
		'object':obj
	}
	return render(request,'product/detail.html',context)


#First
# def product_create_view(request, *args,**kwargs):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ProductForm()
# 	context = {
# 		'form':form
# 	}
# 	return render(request,'product/product_create.html',context)


# def product_create_view(request, *args,**kwargs):
# 	if request.method == "POST":
# 		my_new_title = request.POST.get('title')
# 		print(my_new_title)
# 	context = {}
# 	return render(request,'product/product_create.html',context)

#Second
def product_create_view(request, *args,**kwargs):
	# By default inside the RawProductForm is request.GET
	form = RawProductForm()
	if request.method=="POST":
		form = RawProductForm(request.POST)
		if form.is_valid():
			# form.save() does not exist in the forms.Form
			print(form.cleaned_data)
			#** turn form.cleaned_data as an argument that we gonna pass
			Product.objects.create(**form.cleaned_data)
			form = RawProductForm()
		else:
			print(form.errors)
	context = {
		"form":form
	}
	return render(request,'product/product_create.html',context)