from django.shortcuts import render
from django.http.response import HttpResponse , JsonResponse
from .models import Khedmat , Doctor ,Nobat
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serialize import CopunSerializer , Transcreate , Factorserialize
from rest_framework.permissions import IsAuthenticated , IsAdminUser ,AllowAny , 
from rest_framework_simplejwt.views import TokenObtainPairView , token_refresh

class login(TokenObtainPairView):
    pass

class refresh(token_refresh):
    pass

class NobatDetail(ListCreateAPIView):
    queryset = Nobat.objects.all()
    serializer_class = NobatSerializer
    def get_permissions(self):
        if self.action == 'POST':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'GET':
            self.permission_classes =[AllowAny]
        return super().get_permissions()
# Create your views here.
