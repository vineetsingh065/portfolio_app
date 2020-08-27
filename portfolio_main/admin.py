from django.contrib import admin
from .models import Main, TechnicalSkills, Experience, Accomplishment, Interests, Education

# Register your models here.
admin.site.register(Main)
admin.site.register(TechnicalSkills)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Accomplishment)
admin.site.register(Interests)