from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from time import sleep

def main_page(request):
    return render(request, 'main.html')

def login_page(request):
    return render(request, 'login.html')

def login_action(request):
    id = request.GET.get("id", "")
    pwd = request.GET.get("pwd", "")

    print("12312")

    # 디비 id 조회 후 패스워드 비교
    
    return JsonResponse({'success' : id == "12"})

def register_page(request):
    return render(request, 'register.html')