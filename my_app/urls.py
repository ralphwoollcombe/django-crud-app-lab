from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('people/', views.PersonList.as_view(), name='person-index'),
    path('people/<int:pk>/', views.PersonDetail.as_view(), name='person-detail'),
    path('people/create/', views.PersonCreate.as_view(), name='person-create'),
    path('people/<int:pk>/update', views.PersonUpdate.as_view(), name='person-update'),
    path('people/<int:pk>/delete', views.PersonDelete.as_view(), name='person-delete'),
    path('people/<int:pk>/add-encounter/', views.add_encounter, name='add-encounter'),

    path('interests/create/', views.InterestCreate.as_view(), name='interest-create'),
    path('interests/', views.InterestList.as_view(), name='interest-index'),
    path('interests/<int:pk>/', views.InterestDetail.as_view(), name='interest-detail'),
    path('interests/<int:pk>/update/', views.InterestUpdate.as_view(), name='interest-update'),
    path('interests/<int:pk>/delete/', views.InterestDelete.as_view(), name='interest-delete'),
    path('people/<int:person_id>/associate-interest/<int:interest_id>/', views.associate_interest, name='associate-interest'),
    path('people/<int:person_id>/remove-interest/<int:interest_id>/', views.remove_interest, name='remove-interest'),

    path('accounts/signup/', views.signup, name='signup')
]
