from django.urls import path
from . import views


urlpatterns= [
	path('',views.index,name='index'),
	path('about',views.about,name='about'),
	path('contact',views.contact,name='contact'),
	path('catalog',views.catalog,name='catalog'),
	path('proje',views.proje,name='proje'),	
	path('sistem/<str:sistem_url>',views.sistem,name='sistem'),

]