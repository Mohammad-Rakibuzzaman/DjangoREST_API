# adding urls for views.py
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('create', CreateTodo.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view())

]

#Now again back settings file and declare third party app