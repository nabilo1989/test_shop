from django.shortcuts import render, get_object_or_404


def home(request, slug=None):
    return render(request, 'core/home.html')
