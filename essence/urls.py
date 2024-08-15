from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog', views.blog, name='blog'),
    path('blog_details', views.blog_details, name='blog_details'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('product_details', views.product_details, name='product_details'),
    path('regular_page', views.regular_page, name='regular_page'),
    path('shop', views.shop, name='shop'),
]
