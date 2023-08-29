from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length


def display_topic(request):
    QSTO=Topic.objects.all()
    d={'topics':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO=Webpage.objects.all()
    d={'web':QSWO}
    return render(request,'display_webpage.html',d)

def display_acessrecords(request):
    QSARO=Accessrecords.objects.all()
    d={'records':QSARO}
    return render(request,'display_acessrecords.html',d)


def Insert_Topic(request):
    tn=input('Enter topic_name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()

    QSTO=Topic.objects.all()
    d={'topics':QSTO}
    return render(request,'display_topic.html',d)


def Insert_Webpage(request):
    tn=input('Enter topic_name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('Enter Name : ')
    u=input('Enter url : ')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()

    QSWO=Webpage.objects.all()
    d={'web':QSWO}
    return render(request,'display_webpage.html',d)

def Insert_AccessRecords(request):
    tn=input('Enter topic_name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('Enter Name : ')
    u=input('Enter url : ')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()

    d=input('Enter date : ')
    a=input('Enter Author : ')
    ao=Accessrecords.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()

    QSARO=Accessrecords.objects.all()
    d={'records':QSARO}
    return render(request,'display_acessrecords.html',d)