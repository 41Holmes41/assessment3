from django.shortcuts import render, redirect
from .models import Item
from django.views.generic.edit import CreateView

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  item_list=Item.objects.all()
  return render(request, 'about.html', {'item_list': item_list})

""" def add(request):
  return render(request, 'add.html') """

class create(CreateView):
  model = Item
  fields = ['description']

def remove(request, item_id):
  Item.objects.filter(id=item_id).delete()
  return redirect('home')