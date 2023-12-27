from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('contact', views.contact, name= 'contact'),
    path('product_de/<slug:slug>/',views.product_de, name='product_de'),
    path('cap', views.cap, name='cap'),
    path('product',views.product, name="product"),
    path('cart',views.cart,name='cart'),
    path('test',views.test,name='test'),
    path('register',views.register, name ='register'),
    path('login',views.login ,name ='login'),
]
 