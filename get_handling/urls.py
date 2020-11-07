from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('make/<url>', views.create),
    path('<shortURL>', views.redirecturl)
]
