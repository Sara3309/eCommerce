from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'home$',views.home),
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'menu$',views.menu),
    url(r'product_detail$', views.product_detail),
    url(r'shopping$', views.shopping),
    url(r'sign_in$', views.signIn),
    url(r'signUp$', views.signUp) ,
    url(r'user$', views.user),
    url(r'edit$', views.edit),
    url(r'order$', views.order),
    url(r'order_detail$', views.order_detail)
]                            