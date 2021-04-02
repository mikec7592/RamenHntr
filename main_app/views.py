from django.shortcuts import render
from .models import Ramen
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def ramen_index(request):
    ramen = Ramen.objects.all()
    return render(request, 'ramen/index.html', {'ramen': ramen})

def ramen_detail(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    return render(request, 'ramen/detail.html', {'ramen': ramen})

class RamenCreate(CreateView):
    model = Ramen
    fields = '__all__'

class RamenUpdate(UpdateView):
    model = Ramen
    fields = '__all__'

class RamenDelete(DeleteView):
    model = Ramen
    success_url = '/ramen/'
