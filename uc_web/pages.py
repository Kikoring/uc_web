from django.shortcuts import render
from .models import Memo

def main(request):
    memos = Memo.objects.values();

    context = {
        'memos': memos,
    }

    return render(request, 'main.html', context)

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def add_post(request):
    return render(request, 'addPost.html')

def post_detail(request, id):
    memo = Memo.objects.get(id=id)

    context = {
        'memo': memo,
    }
    
    return render(request, 'postDetail.html', context)