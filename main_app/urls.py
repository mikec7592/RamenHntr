from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ramen/',  views.ramen_index, name='index'),
    path('ramen/<int:ramen_id>/', views.ramen_detail, name='detail'),
]