from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def starter(request):
    return render(request, 'starter-page.html')
