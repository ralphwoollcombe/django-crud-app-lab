from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('person/', views.person_index, name='person-index'),
    path('person/<int:person_id>/', views.person_detail, name='person-detail')
]
