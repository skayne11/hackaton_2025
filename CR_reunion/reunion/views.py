from django.shortcuts import render
from .models import Reunion

def liste_reunions(request):
    reunions = Reunion.objects.all().order_by('-date')
    return render(request, 'reunion.html', {'reunions': reunions})
