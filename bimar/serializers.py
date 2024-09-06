from .models import Khedmat , Nobat
from rest_framework import serializers



class Nobatserializer(serializers.ModelSerializer):
    
    class meta:
        model = Nobat
        field = '__all__'


class Khedmatserializer(serializers.ModelSerializer):
    class meta:
        model = Khedmat
        field = '__all__'

    
