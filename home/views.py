from django.shortcuts import render


def index_view(request):
    return render(request, "home/index.html")


def about_view(request):
    return render(request, "home/about.html")
