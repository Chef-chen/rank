from django.urls import path
from test_API import views

urlpatterns = [
    path('upload/', views.upload,),
    path('show', views.show, ),

]
