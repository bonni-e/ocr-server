from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import User
from .serializers import *

class Login(APIView) :
    def post(self, request) :
        user = authenticate(
            request,
            username = request.data.get('username'),
            password = request.data.get('password')
        )

        if user :
            login(request, user)
            return Response({'auth' : True})  
        else :
            return Response({'auth' : False})  

class Logout(APIView) :
    permission_classes = [IsAuthenticated]

    def post(self, request) :
        logout(request)
        request.session.flush()
        # return redirect("/boards")
        return HttpResponseRedirect("/boards")

class Users(APIView) :
    def post(self, request) :
        serializer = UserRequestSerializer(data=request.data)
        if serializer.is_valid() :
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(UserOverviewSerializer(user).data)
        else :
            return Response(serializer.errors)

class UserList(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request) :
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        admin = User.objects.get(username='admin')
        if request.user == admin :
            return Response(serializer.data)
        else :
            raise PermissionDenied

class UserDetail(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request, pk) :
        user = self.get_object(request, pk)
        serializer = UserOverviewSerializer(user)

        return Response(serializer.data)
    
    def put(self, request, pk) :
        user = self.get_object(request, pk)
        serializer = UserRequestSerializer(user, data=request.data, partial=True)

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        
    def delete(self, request, pk) :
        user = self.get_object(request, pk)
        user.delete()
        return Response(HTTP_204_NO_CONTENT)

    def get_object(self, request, pk) :
        try :
            user = User.objects.get(pk=pk)
            if user == request.user :
                return user
            else :
                raise PermissionDenied
        except User.DoesNotExist :
            raise NotFound
