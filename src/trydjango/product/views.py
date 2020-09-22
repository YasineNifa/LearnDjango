from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

from .forms import ProductForm

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



# def product_create_view(request, *args,**kwargs):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ProductForm()
# 	context = {
# 		'form':form
# 	}
# 	return render(request,'product/product_create.html',context)


def product_create_view(request, *args,**kwargs):
	if request.method == "POST":
		my_new_title = request.POST.get('title')
		print(my_new_title)
	context = {}
	return render(request,'product/product_create.html',context)