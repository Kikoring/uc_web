from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from .models import User, Memo

# Auth


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("id")
        password = request.POST.get("pwd")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "message": "로그인 실패"})

    return JsonResponse({"success": False, "message": "잘못된 요청"}, status=400)


def register(request):
    if request.method == "POST":
        username = request.POST.get("id")
        password = request.POST.get("pwd")
        nickname = request.POST.get("nickname")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "message": "이미 존재하는 아이디입니다."})

        if User.objects.filter(nickname=nickname).exists():
            return JsonResponse({"success": False, "message": "이미 존재하는 닉네임입니다."})

        user = User.objects.create_user(
            username=username, password=password, nickname=nickname)
        user.save()

        return JsonResponse({"success": True, "message": "회원가입 성공!"})

    return JsonResponse({"success": False, "message": "잘못된 요청"}, status=400)


def csrf_token(request):
    """CSRF 토큰을 JSON으로 반환"""
    return JsonResponse({"csrfToken": get_token(request)})

# Posts


def posts(request):
    if request.method == "POST":
        if request.user is None:
            return JsonResponse({"success": False, "message": "로그인 필요"})

        title = request.POST.get("title")
        content = request.POST.get("content")

        memo = Memo.objects.create(
            title=title, content=content, user=request.user,)

        return JsonResponse({"success": True, "message": "작성 성공!", "id": memo.id})

    return JsonResponse({"success": False, "message": "잘못된 요청"}, status=400)
