from .models import UserAppModel
from .serializer import UserAppSerializer
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
import logging
from django.contrib.auth.models import auth


# Create your views here.


class UserRegister(APIView):
    logger = logging.getLogger(__name__)

    def post(self, request):
        """
        Register user with given details
        :param request:
        :return: http response
        """
        try:
            user_dict = UserAppSerializer(data=request.data)
            if user_dict.is_valid():
                user = UserAppModel.objects.create_user(username=user_dict.data['username'],
                                                        email=user_dict.data['email'],
                                                        password=user_dict.data['password'],
                                                        first_name=user_dict.data['first_name'],
                                                        last_name=user_dict.data['last_name'],
                                                        )
                user = UserAppSerializer(user)
                return JsonResponse({"message": "User successfully registered", "data": user.data['username']})
            return HttpResponse("Invalid Data provided")
        except Exception as e:
            self.logger.exception(e)
            return HttpResponse("Error occurred")


class UserLogin(APIView):
    logger = logging.getLogger(__name__)

    def get(self, request):
        """
        Get first_name of all our users
        :param request:
        :return:
        """
        try:
            users = UserAppModel.objects.all()
            user_objects = UserAppSerializer(users, many=True)
            list_of_users = []
            for user in user_objects.data:
                list_of_users.append(user["first_name"])
            return JsonResponse({"message": "fetched all", "Data": list_of_users})
        except Exception as e:
            self.logger.exception(e)
            HttpResponse("error at getting details")

    def post(self, request):
        """
        Checks whether username and password exist in our database and logs in
        :param request:
        :return: http response
        """

        try:
            user_dict = UserAppSerializer(data=request.data)
            is_user_exist = auth.authenticate(username=user_dict.initial_data.get("username"),
                                              password=user_dict.initial_data.get("password"))
            if is_user_exist:
                return JsonResponse({"message": "Successfully logged in"})
            else:
                return JsonResponse({"message": "Invalid Credentials"})
        except Exception as e:
            self.logger.exception(e)
            return JsonResponse({"message": "error occurred"})
