from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Ramen:
    def __init__(self, name, price, description, rating):
     self.name = name
     self.price = price
     self.description = description
     self.rating = rating 

ramen= [
    Ramen('Kogane', '$$', 'One of my go to spots', 8),
    Ramen('Naruto', '$$$', 'Over-rated but good', 6),
    Ramen('Test Spot', '$$$$', 'Wonder how this is gonna look after some work', 2)
]

def home(request):
    return HttpResponse('<h1>YYUUURRRRR</h1>')
def about(request):
    return render(request, 'about.html')
def ramen_index(request):
    return render(request, 'ramen/index.html', {'ramen': ramen})