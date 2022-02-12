from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

from .models import User
from django.http import JsonResponse
import json


def user_registration(request):
    """
    Register user with given details
    :param request:
    :return: http response
    """
    if request.method == "POST":
        try:
            user_dict = json.loads(request.body)
            if User.objects.filter(user_name=user_dict.get("user_name")).exists():
                return JsonResponse({"message": "User is already Registered"})

            first_name = user_dict.get("first_name")
            last_name = user_dict.get("last_name")
            user_name = user_dict.get("user_name")
            user_password = user_dict.get("user_password")
            email = user_dict.get("email")
            number = user_dict.get("number")

            user = User(first_name=first_name, last_name=last_name, user_name=user_name, user_password=user_password,
                        email=email, number=number)
            user.save()
            return JsonResponse({"message": "User Registered Successfully", "data": user_dict})
        except Exception:
            return JsonResponse({"message": "Data is invalid"})
    return JsonResponse({"expected": "POST method", "provided": "GET method"})

def login(request):
    """
    Checks whether username and password exist in our database
    :param request:
    :return: http response
    """
    if request.method == "POST":
        try:
            user_dict = json.loads(request.body)
            if User.objects.filter(user_name=user_dict.get("user_name"),
                                   user_password=user_dict.get("user_password")).exists():
                return JsonResponse({"message": "Successfully logged in"})
        except Exception:
            return JsonResponse({"message": "Invalid Credentials"})
    return JsonResponse({"expected": "POST method", "provided": "GET method"})

def get_user_details(request):
    """
    Get details of all our users
    :param request:
    :return:
    """
    if request.method == "GET":
        try:
            users = User.objects.all()
            list_of_users = []
            for user in users:
                data = {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "user_name": user.user_name,
                    "user_password": user.user_password,
                    "email": user.email,
                    "number": user.number
                }
                list_of_users.append(data)
            return JsonResponse({"message": "fetched all", "Data": list_of_users})
        except Exception:
            HttpResponse("error at getting details")
    return JsonResponse({"expected": "POST method", "provided": "GET method"})

