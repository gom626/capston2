from django.shortcuts import render
import json
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Account
from django.shortcuts import redirect

# Create your views here.


class signupiView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email = data['email']).exists():
                 return HttpResponse(status=400)
            Account.objects.create(
               email = data['email'],
               password = data['password']
               #nickname = data['nickname']
               #sex= data['sex']
               )
            return JsonResponse({'message': '회원가입 성공'},status=200)
        except keyError:
            return JsonResponse({"message":"INVALID_KEYS"},status=400)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        if Account.objects.filter(email = data['email']).exists() :
            user = Account.objects.get(email = data['email'])
            if user.password == data['password'] :
                return JsonResponse({'message':f'{user.email}님 로그인 되셨습니다.'}, status=200)
            else :
                return JsonResponse({'message':'비밀번호가 틀렸어요'},status = 401)

        return JsonResponse({'message':'미등록 이메일 입니다.'},status=400)

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"],last_name=request.POST["nickname"])
            auth.login(request,user)
            return redirect('home')
        return render(request,'signup.html')
    return render(request,"signup.html")


def login(request):
    if request.method =="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error': 'username or password is incorrect'})
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('home')
