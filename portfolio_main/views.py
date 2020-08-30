from django.shortcuts import render
from .models import Main, TechnicalSkills, Experience, Education, Accomplishment, Projects

# Create your views here.


def home(request):
    main = Main.objects.get(pk=1)
    ts = TechnicalSkills.objects.all()
    exp = Experience.objects.all()
    edu = Education.objects.all()
    accom = Accomplishment.objects.all()
    proj = Projects.objects.all()

    return render(request, 'front/index.html', {'details': main, 'ts':ts, 'exp': exp, 'edu': edu, 'accom': accom,
                                                'proj':proj})