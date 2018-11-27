from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name="main"),
	url(r'^contact/', views.contact, name="contact"),
	url(r'^products/', views.products, name="products"), 
]
