from django.contrib import admin
from django.urls import path
from rest_framework import routers

from app import views


routers = routers.SimpleRouter(trailing_slash=False)
routers.register('Book', views.BookView,'Book')
# routers.register('Author', views.AuthorView,'Author')

urlpatterns = [
]

urlpatterns += routers.urls