from django.urls import path
from .import views

urlpatterns = [
    path('pharmacy/',views.pharmacy,name='pharmacy'),
    path('category_sort/<slug:category_slug>/',views.category_sort, name='category_sort'),
    path('product_details/<slug:product_slug>/',views.product_details,name='product_details'),
    
]