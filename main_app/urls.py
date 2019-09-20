from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
   path('create/', views.create.as_view(), name="create"),
   path('delete/<int:item_id>', views.remove, name="delete"),

   #path('add/', views.add, name="add"),
]