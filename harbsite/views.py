from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "harbsite/index.html")

def about(request):
    return render(request, "harbsite/about.html")

def author(request):
    return render(request, "harbsite/author.html")

def get_the_book(request):
    return render(request, "harbsite/get_the_book.html")