from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *


def insert_topic(request):
    if request.method=='POST': 
         topic_name=request.POST['tn']  
         to=Topic.objects.get_or_create(topic_name=topic_name)[0]
         to.save()
         return HttpResponse('insert data in topic')
    return render(request,'insert_topic.html')



def insert_webpage(request):
     if request.method=='POST':
        topic_name=request.POST['tn']
        name=request.POST.get('n')
        url=request.POST.get('u')
        email=request.POST.get('em')
        to=Topic.objects.get(topic_name=topic_name)
        wo=Webpage.objects.get_or_create(topic_name=to,name=name,url=url,email=email)[0]
        wo.save()
        return HttpResponse('insert data in webpage')
     return render(request,'insert_webpage.html')


def insert_access(request):
    if request.method=='POST':
        name=request.POST['n']
        date=request.POST.get('d')
        author=request.POST.get('au')
        wo=Webpage.objects.get(name=name)
        ao=AccessRecord.objects.get_or_create(name=wo,date=date,author=author)[0]
        ao.save()
        return HttpResponse('insert data in accessrecord')
    return render(request,'insert_access.html')

