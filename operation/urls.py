
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('add',views.add),
    path('update/<int:pk>',views.update),
    path('delete/<int:pk>',views.delete)

]