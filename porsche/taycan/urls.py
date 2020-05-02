from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='taycan-home'),
    path('nextpage/', views.nextpage, name='taycan-next'),
    path('cr/', views.CR, name='taycan-CR'),
    path('or/', views.OR, name='taycan-OR'),
]
