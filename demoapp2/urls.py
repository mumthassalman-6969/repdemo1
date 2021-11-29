from django.urls import path
from  . import views
urlpatterns=[
    path('user/',views.fnabc, name='user'),
    path ('abc/',views.fnmno,name='abc')
]