from .models import Khedmat , Nobat
from rest_framework import serializers



class Nobatserializer(serializers.ModelSerializer):
    
    class meta:
        model = Nobat
        fields = '__all__'


class Khedmatserializer(serializers.ModelSerializer):
    class meta:
        model = Khedmat
        fields = '__all__'

    
