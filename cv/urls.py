from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.cv, name='cv'),
    path('cv/new/', views.cv_new, name='cv_new'),
    path('cv/<int:pk>/edit/', views.cv_edit, name='cv_edit'),
]