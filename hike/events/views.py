from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage 
from .models import events , discussion, player
from django.contrib import admin
import datetime

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
    discussion_list = discussion.objects.filter(eventsId=eid).order_by('-subTime');
    return render(request,'detail.html',locals())

def board(request,bpage=1):
    ats = discussion.objects
    
    paginator = Paginator(ats,2)

    pageInfo = paginator.page(page)

    return HttpResponse(pageInfo.number)

def add_discussion(request):
    message = request.POST.get('message');
    user_id = request.session.get('_auth_user_id');
    _player = player.objects.filter(playerId=user_id).first();
    eventsId = request.POST.get('eventsId');
    det = events.objects.filter(id=eventsId).first();
    discussion.objects.create(eventsId=det,playerId=_player,playerName=_player.playerName,message='踩一下',subTime = datetime.datetime.now());
    return render(request,'detail.html',locals())