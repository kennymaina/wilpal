from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^about/', views.about, name='about'),
    url(r'^air/', views.air, name='air'),

    url(r'^contact/$', views.contact, name='contacts'),
    url(r'^services/', views.services, name='services'),
    
]