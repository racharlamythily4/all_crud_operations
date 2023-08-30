from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

'''Display Topics'''
def display_topic(request):
    QSTO=Topic.objects.all()
    QSTO=Topic.objects.filter(topic_name='Cricket')
    QSTO=Topic.objects.exclude(topic_name='Cricket')
    QSTO=Topic.objects.all()
    QSTO=Topic.objects.filter(topic_name__contains='ba')
    QSTO=Topic.objects.all()
    d={'topics':QSTO}
    return render(request,'display_topic.html',d)

'''Display Webpages'''
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

    QSWO=Webpage.objects.filter(Q(name__contains='a')&Q(url__endswith='in'))
    QSWO=Webpage.objects.filter(url__regex='com$')
    QSWO=Webpage.objects.filter(Q(url__regex='in$')&Q(pk__gt='3'))
    QSWO=Webpage.objects.all()

    
    d={'web':QSWO}
    return render(request,'display_webpage.html',d)
'''Display AccessRecords'''
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

    QSARO=Accessrecords.objects.filter(Q(date__year__gt='2000')|Q(author__contains='a'))
    QSARO=Accessrecords.objects.filter(Q(author__regex='l')&Q(date__regex='\d'))
    QSARO=Accessrecords.objects.all()


    d={'records':QSARO}
    return render(request,'display_acessrecords.html',d)

'''Insert Topics'''
def Insert_Topic(request):
    tn=input('Enter topic_name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()

    QSTO=Topic.objects.all()
    d={'topics':QSTO}
    return render(request,'display_topic.html',d)

'''Insert Webpages'''
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
'''Insert AccesRecords'''
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

'''Upadte Topics'''
def update_topic(request):
    QSTO=Topic.objects.all()
    d={'topics':QSTO}
    return render(request,'display_topic.html',d)

'''Update Webpages'''

def update_webpage(request):
    
    '''UPDATE METHOD'''
    '''One row can be satisfies'''
    #Webpage.objects.filter(name='Mythily Racharla').update(name='Racharla Mythily')
    #Webpage.objects.filter(topic_name='Virat').update(topic_name='Cricket')
    #Webpage.objects.filter(name='Racharla Mythily').update(name='Hardik')
    '''Multiple rows can be satisfied'''
    #Webpage.objects.filter(topic_name='Cricket').update(url='https://cricket.in')
    '''No operations will be performed'''
    #Webpage.objects.filter(name='Racharla Mythily').update(name='Hardik')
    '''Foreign key constraint failed(because we need to provide values which are present in parent table)'''
    #Webpage.objects.filter(topic_name='Kabaddi').update(topic_name='Hockey')

    '''UPDATE_OR_CREATE METHOD'''
    '''One row satisfies'''

    #OB=Topic.objects.get(topic_name='Football')
    #Webpage.objects.update_or_create(name='Sindhu',defaults={'topic_name':OB,'url':'http://Football.com'})

    '''Multiple rows can't be satisfies because(we can't modify multiple rows by update_or_create method)'''

    #OB=Topic.objects.get(topic_name='Cricket')
    #Webpage.objects.update_or_create(topic_name='Cricket',defaults={'topic_name':OB,'topic_name':'CRICKET'})

    '''No Rows Satisfies(It will create a new row)'''
    #OB=Topic.objects.get(topic_name='Cricket')
    #Webpage.objects.update_or_create(name='virat',defaults={'topic_name':OB,'name':'kohli'})

    #OB=Topic.objects.get(topic_name='Football')
    #Webpage.objects.update_or_create(name='ani',defaults={'topic_name':OB,'name':'Anitha'})

        
    QSWO=Webpage.objects.all()
    d={'web':QSWO}
    return render(request,'display_webpage.html',d)

'''Update Accessrecords'''
def update_acessrecords(request):

    QSARO=Accessrecords.objects.all()
    d={'records':QSARO}
    return render(request,'display_acessrecords.html',d)

'''Delete Webpage'''
def delete_webpage(request):
    Webpage.objects.filter(name='Anitha').delete()
    Webpage.objects.filter(name='kohli').delete()
    QSWO=Webpage.objects.all()
    d={'web':QSWO}
    return render(request,'display_webpage.html',d)