from django.urls import path
from . import views

urlpatterns = [
    path("", views.test),
    path("book/", views.book_list)
]
