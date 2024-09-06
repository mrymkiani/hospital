from django.shortcuts import render
from django.http.response import HttpResponse , JsonResponse
from .models import Khedmat , Doctor ,Nobat
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import Khedmatserializer , Nobatserializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser ,AllowAny 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .permissions import IsSuperUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from .serializers import Nobatserializer, Khedmatserializer


class login(TokenObtainPairView):
    pass

class refresh(TokenRefreshView):
    pass

class NobatDetail(ListCreateAPIView):
    queryset = Nobat.objects.all()
    serializer_class = Nobatserializer
    filter_backends = [DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["bimar_name"]
    filterset_fields = ['date',"time"]
    def get_permissions(self):
        if self.action == 'POST':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'GET':
            self.permission_classes =[IsAuthenticated]
    def get_queryset(self):
        return Nobat.objects.filter(user=self.request.user)
    
class EditNobat(RetrieveUpdateDestroyAPIView):
    queryset = Nobat.objects.all()
    serializer_class = Nobatserializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        return Nobat.objects.filter(user=self.request.user)
    
class CreatKhedmat(CreateAPIView):
    queryset = Khedmat.objects.all()
    serializer_class = Khedmatserializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        return Khedmat.objects.filter(user=self.request.user)
    
class Payment(ListAPIView):
    queryset = Nobat.objects.filter(pay_status = 'True')
    serializer_class = Nobatserializer
    filter_backends = [DjangoFilterBackend , filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['date']
    permission_classes = [IsSuperUser]
    def get_queryset(self):
        return Nobat.objects.filter(user=self.request.user)
    


    
