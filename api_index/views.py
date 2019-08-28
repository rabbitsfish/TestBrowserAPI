from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def en_de(request):
    return redirect('/base_tools/en_de_index/')

def to_transform_api_sign(request):
    return redirect('/browser_api/api_sign/')