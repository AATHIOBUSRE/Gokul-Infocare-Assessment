from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('getcontact/',views.getcontact),
    path('updatec/<int:pk>',views.updatec)
]
