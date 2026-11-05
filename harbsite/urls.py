from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("author/", views.author, name="author"),
    path("get-the-book/", views.get_the_book, name="get_the_book"),
]