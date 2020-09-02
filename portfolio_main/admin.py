from django.contrib import admin
from .models import Main, TechnicalSkills, Experience, Accomplishment, Projects, Education, Recommendations

# Register your models here.
admin.site.register(Main)
admin.site.register(TechnicalSkills)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Accomplishment)
admin.site.register(Projects)
admin.site.register(Recommendations)