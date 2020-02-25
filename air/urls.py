from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^about/', views.about, name='about us'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^services/', views.services, name='services'),
    
]