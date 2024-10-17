from django.shortcuts import render
from .models import ProgrammerResume

def index(request):
    resume = ProgrammerResume.objects.first()
    return render(request, 'programmer_resume/index.html', {'resume': resume})
