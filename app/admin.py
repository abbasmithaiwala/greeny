from django.contrib import admin
from app.models import *

class Contactforadmin(admin.ModelAdmin):
    list_display = ["name","email","message","subject"]
admin.site.register(Contact,Contactforadmin)  


class Aboutforadmin(admin.ModelAdmin):
  list_display = ["number","name","content"]
admin.site.register(About,Aboutforadmin)

class Teamforadmin(admin.ModelAdmin):
  list_display = ["name","destination","img","content"]
admin.site.register(Team,Teamforadmin)  
