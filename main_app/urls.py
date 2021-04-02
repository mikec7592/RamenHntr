from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ramen/',  views.ramen_index, name='index'),
    path('ramen/<int:ramen_id>/', views.ramen_detail, name='detail'),
    path('ramen/create', views.RamenCreate.as_view(), name='ramen_create'),
    path('ramen/<int:pk>/update/', views.RamenUpdate.as_view(), name='ramen_update'),
    path('ramen/<int:pk>/delete/', views.RamenDelete.as_view(), name='ramen_delete'),
]