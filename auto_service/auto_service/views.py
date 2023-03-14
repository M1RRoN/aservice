from django.shortcuts import render


def index(request):
    return render(request, 'auto_service/index.html')