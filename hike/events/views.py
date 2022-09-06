from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage 
from .models import events , discussion

# Create your views here.

def article(request,page=1):
    ats = events.objects.filter(status=0).order_by('-createTime')
    paginator = Paginator(ats,2)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger :
        pageInfo = paginator.page(1)
    except EmptyPage :
        pageInfo = paginator.page(paginator.num_pages)
            
    return render(request,'article.html',locals())


def detail(request,eid):
    det=events.objects.filter(id=eid).first()

    return render(request,'detail.html',locals())

def board(request,bpage=1):
    ats = discussion.objects
    
    paginator = Paginator(ats,2)

    pageInfo = paginator.page(page)

    return HttpResponse(pageInfo.number)