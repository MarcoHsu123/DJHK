from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage 
from .models import events

# Create your views here.

def article(request,page=1):
    ats = events.objects.filter(status=0).order_by('-createTime')
    paginator = Paginator(ats,10)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger :
        pageInfo = paginator.page(1)
    except EmptyPage :
        pageInfo = paginator.page(paginator.num_pages)
            
    return render(request,'article.html',locals())

def hike(request,page=1):
    ats = events.objects.filter(status=0).order_by('-createTime')
    paginator = Paginator(ats,10)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger :
        pageInfo = paginator.page(1)
    except EmptyPage :
        pageInfo = paginator.page(paginator.num_pages)

    return HttpResponse(page)