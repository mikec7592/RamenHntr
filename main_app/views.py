from django.shortcuts import render
from .models import Ramen

# Create your views here.

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def ramen_index(request):
    ramen = Ramen.objects.all()
    return render(request, 'ramen/index.html', {'ramen': ramen})