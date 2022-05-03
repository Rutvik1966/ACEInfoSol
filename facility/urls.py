from django.urls import path,include
from . import views
urlpatterns = [
    path('services/webdevelopment', views.index,name='web'),
    path('services/e-commerce', views.ecom,name='ecom'),
    path('services/digital-marketing', views.digi,name='digi'),
    path('services/ui-ux', views.ux,name='ux'),
    path('services/softwaredev', views.dev,name='dev'),
    path('services/ml-ai', views.ml,name='ai'),
]