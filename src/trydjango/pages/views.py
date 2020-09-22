from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# it will handle our web page variables
def home_view(request,*args,**kwargs):
	print(request)
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request,"home.html",{})#template name, context

def contact_view(request,*args,**kwargs):
	# return HttpResponse("<h1>Contact Page</h1>")
	return render(request,'contact.html',{})

def about_view(request,*args,**kwargs):
	print(request)
	#<WSGIRequest: GET '/about/'>
	print(request.user)
	#yassine
	# return HttpResponse("<h1>About Page</h1>")
	my_context = {
		"my_text":"this is about us",
		"my_number": 123,
		"my_list" : [1,2,3,4,7],
		"my_html":"<h6>Hello there</h6>"
	}
	return render(request,'about.html',my_context)

# Context can be any dat type
