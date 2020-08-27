from django.shortcuts import render
from .models import Main

# Create your views here.


def home(request):
    st = Main.objects.get(pk=1)
    print(st.user_pic.url)


    return render(request, 'index.html')