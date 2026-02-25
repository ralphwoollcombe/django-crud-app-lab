from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('person/', views.PersonList.as_view(), name='person-index'),
    path('person/<int:pk>/', views.PersonDetail.as_view(), name='person-detail'),
    path('person/create/', views.PersonCreate.as_view(), name='person-create'),
    path('person/<int:pk>/update', views.PersonUpdate.as_view(), name='person-update'),
    path('person/<int:pk>/delete', views.PersonDelete.as_view(), name='person-delete'),
    path('cats/<int:pk>/add-encounter/', views.add_encounter, name='add-encounter'),

]
