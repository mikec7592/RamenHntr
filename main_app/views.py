from django.shortcuts import render, redirect
from .models import Ramen, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'ramenhntrbucket'

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

def add_photo(request, ramen_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # creates a unique key for each photo
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # making relation between models
            photo = Photo(url=url, ramen_id=ramen_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
            print(photo)
    return redirect('detail', ramen_id=ramen_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Adding user to database
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class RamenCreate(CreateView):
    model = Ramen
    fields = ['name', 'price', 'description','rating']
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class RamenUpdate(UpdateView):
    model = Ramen
    fields = '__all__'

class RamenDelete(DeleteView):
    model = Ramen
    success_url = '/ramen/'
