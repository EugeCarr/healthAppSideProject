from django.shortcuts import render
import requests
import os


def index(request):

    return render(request, 'dietapp/index.html')


