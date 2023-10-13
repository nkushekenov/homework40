from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

def home(request):
    return render(request, 'home.html')


def account(request):
    return render(request, 'account.html')


def profile(request):
    return render(request, 'profile.html')