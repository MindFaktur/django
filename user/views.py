from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import User
from django.http import JsonResponse
import json
from .serializer import UserSerializer


class UserRegister(APIView):

    def post(self, request):
        """
        Register user with given details
        :param request:
        :return: http response
        """
        try:
            user_dict = UserSerializer(data=request.data)
            if user_dict.is_valid():
                user_dict.save()
                return JsonResponse({"message": "User successfully registered", "data": user_dict})
            return HttpResponse("Invalid Data provided")
        except Exception as e:
            print(e)
            return HttpResponse("Error occurred")

    def get(self, request):
        """
        Get first_name of all our users
        :param request:
        :return:
        """
        try:
            users = User.objects.all()
            user_objects = UserSerializer(users, many=True)
            list_of_users = []
            for user in user_objects.data:
                list_of_users.append(user["first_name"])
            return JsonResponse({"message": "fetched all", "Data": list_of_users})
        except Exception:
            HttpResponse("error at getting details")


class UserLogin(APIView):

    def post(self, request):
        """
        Checks whether username and password exist in our database and logs in
        :param request:
        :return: http response
        """

        try:
            user_dict = UserSerializer(data=request.data, many=True)
            if User.objects.filter(user_name=user_dict.initial_data.get("user_name"),
                                   user_password=user_dict.initial_data.get("user_password")).exists():
                return JsonResponse({"message": "Successfully logged in"})
            else:
                return JsonResponse({"message": "Invalid Credentials"})
        except Exception as e:
            print(e)
            return JsonResponse({"message": "error occurred"})

