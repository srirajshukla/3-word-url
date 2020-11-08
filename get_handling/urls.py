from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('all', views.viewall),
    path('all/', views.viewall),
    path('<shortURL>', views.redirecturl),
]
