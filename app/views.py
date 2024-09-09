from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    AboutContent = About.objects.all()
    TeamContent = Team.objects.all()
    context ={
    'AboutContent' : AboutContent,

    'TeamContent':TeamContent,
  }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        # Save data to the database
        contact_message = Contact(name=name, email=email, message=message,subject=subject)
        contact_message.save()

        return HttpResponse('Message submitted successfully!') 
    return render(request, 'index.html',context)