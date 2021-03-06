from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product

from .forms import ProductForm

# Create your views here.

def dynamic_lookup_view(request,id):
	# obj = Product.objects.get(id=id)
	obj = get_object_or_404(Product,id=id)
	context={
		"object":obj
	}
	return render(request,"product/detail.html",context)







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
def product_create_view(request, *args,**kwargs):
	form = ProductForm()
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			form = ProductForm()
	context = {
		'form':form
	}
	return render(request,'product/product_create.html',context)


# def product_create_view(request, *args,**kwargs):
# 	if request.method == "POST":
# 		my_new_title = request.POST.get('title')
# 		print(my_new_title)
# 	context = {}
# 	return render(request,'product/product_create.html',context)

#Second
# def product_create_view(request, *args,**kwargs):
# 	# By default inside the RawProductForm is request.GET
# 	form = RawProductForm()
# 	if request.method=="POST":
# 		form = RawProductForm(request.POST)
# 		if form.is_valid():
# 			# form.save() does not exist in the forms.Form
# 			print(form.cleaned_data)
# 			#** turn form.cleaned_data as an argument that we gonna pass
# 			Product.objects.create(**form.cleaned_data)
# 			form = RawProductForm()
# 		else:
# 			print(form.errors)
# 	context = {
# 		"form":form
# 	}
# 	return render(request,'product/product_create.html',context)


def product_delete_view(request,id):
	obj = Product.objects.get(id=id)
	print("+++++++++++++++++", request.method)
	if request.method == "POST":
		#confirm delete
		print("Iam Here")
		obj.delete()
		print("Product deleted")
		return redirect('../../')
	context = {
		"object" : obj
	}
	return render(request,"product/delete.html",context)


def product_list_view(request):
	liste = []
	all_products = Product.objects.all()
	context = {
		"all_products" : all_products
	}

	return render(request,"product/list.html",context)