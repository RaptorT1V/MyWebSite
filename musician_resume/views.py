from django.shortcuts import render


def index(request):
    return render(request, 'musician_resume/index.html')
