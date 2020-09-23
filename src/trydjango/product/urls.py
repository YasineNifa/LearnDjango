from django.urls import path
from product.views import product_detail_view, product_create_view,dynamic_lookup_view,product_delete_view,product_list_view



urlpatterns = [
    path('<int:id>/',dynamic_lookup_view, name='productdynamic'),
    # path('product/',product_detail_view, name='product'),
    path('create/',product_create_view, name='createproduct'),
    path('<int:id>/delete/',product_delete_view,name="product_delete"),
    path('',product_list_view,name="product_list")
]