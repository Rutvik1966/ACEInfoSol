from django.urls import path,include
from . import views
urlpatterns = [
    path('contactus', views.index,name='cu')
]