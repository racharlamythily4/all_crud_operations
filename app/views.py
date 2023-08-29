from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length


def display_topic(request):
    QSTO=Topic.objects.all()
    QSTO=Topic.objects.filter(topic_name='Cricket')
    QSTO=Topic.objects.exclude(topic_name='Cricket')
    QSTO=Topic.objects.all()
    QSTO=Topic.objects.filter(topic_name__contains='ba')
    QSTO=Topic.objects.all()
    d={'topics':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.filter(topic_name='Football')
    QSWO=Webpage.objects.exclude(topic_name='Football')
    QSWO=Webpage.objects.filter(topic_name='Kabaddi').order_by('name')
    QSWO=Webpage.objects.all().order_by('name')
    QSWO=Webpage.objects.all().order_by('-name')
    QSWO=Webpage.objects.all().order_by(Length('name'))
    QSWO=Webpage.objects.all().order_by(Length('name').desc())
    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.filter(name='chandu')
    QSWO=Webpage.objects.filter(pk__gt=4)
    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.filter(name__startswith='n')
    QSWO=Webpage.objects.filter(url__endswith='com')
    QSWO=Webpage.objects.filter(name__contains='ba')
    QSWO=Webpage.objects.filter(name__in=('shoban','chandu')) 
    QSWO=Webpage.objects.filter(name__regex='^\w')
    QSWO=Webpage.objects.filter(url__regex='[com]')
    QSWO=Webpage.objects.all()

    d={'web':QSWO}
    return render(request,'display_webpage.html',d)

def display_acessrecords(request):
    QSARO=Accessrecords.objects.all()
    QSARO=Accessrecords.objects.filter(author__contains='a')
    QSARO=Accessrecords.objects.filter(date__month='08')
    QSARO=Accessrecords.objects.filter(date__year='1999')
    QSARO=Accessrecords.objects.filter(date__year__gt='1999')
    QSARO=Accessrecords.objects.filter(date__year__gte='1999')
    QSARO=Accessrecords.objects.filter(date__year__lt='1999')
    QSARO=Accessrecords.objects.filter(date__year__lte='1999')
    QSARO=Accessrecords.objects.filter(date__day='06')
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