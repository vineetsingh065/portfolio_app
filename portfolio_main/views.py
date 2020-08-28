from django.shortcuts import render
from .models import Main, TechnicalSkills

# Create your views here.


def home(request):
    main = Main.objects.get(pk=1)
    ts = TechnicalSkills.objects.all()

    return render(request, 'front/index.html', {'details': main, 'ts':ts})