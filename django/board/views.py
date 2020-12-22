from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post
from confluent_kafka import *
import json

def create(request):
    return render(request,'create.html')

def createPost(request):
    if request.method=='POST':
        board=Post()
        board.people=request.POST['people']
        board.title=request.POST['title']
        board.count=1
        board.main_text=request.POST['main_text']
        board.Edate=request.POST['Edate']
        board.Cdate=timezone.datetime.now()
        board.location=request.POST['location']
        board.create_user=User.objects.get(username=request.POST['create_user_id'])
        board.create_img=request.FILES['create_img']
        board.game=request.POST['game']
        board.ALT=request.POST['ALT']
        board.LAT=request.POST['LDT']
        board.save()
        p = Producer({'bootstrap.servers': 'localhost:9092'})
        p.produce(str(board.num), value='Create!')
        p.flush(30)
        messages.info(request, '게시판이 성공적으로 등록되었습니다.')
        return redirect('/board/detail/'+str(board.num))

def detail(request, blog_id):
    blog_detail = get_object_or_404(Post, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def category(request, game):
    queryset = Post.objects.all().filter(game=game)
    return render(request,'category.html',{'post':queryset})

def regist(request,blog_id):
    queryset =Post.objects.get(num=blog_id)
    if queryset.count>=queryset.people:
        messages.info(request, '이미 만원인 방입니다..')
    else:
        queryset.count=queryset.count+1
        queryset.save()
        messages.info(request, '참가완료 하였습니다.')
    return render(request,'detail.html',{'blog':queryset})
