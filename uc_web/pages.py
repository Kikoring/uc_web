from django.shortcuts import render
from .models import Memo, User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def main(request):
    memos = Memo.objects.values();

    context = {
        'memos': memos,
    }

    return render(request, 'main.html', context)

def sign_in(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def add_post(request):
    if request.user.is_authenticated:
        return render(request, 'addPost.html')
    else:
        return render(request, 'login.html')

def post_detail(request, id):
    memo = Memo.objects.get(id=id)

    context = {
        'memo': memo,
    }
    
    return render(request, 'postDetail.html', context)