from .models import Khedmat , Nobat
from rest_framework import serializers



class nobatserializer(serializers.ModelSerializer):
    
    class meta:
        model = Nobat
        field = '__all__'


class khedmatserializer(serializers.ModelSerializer):
    class meta:
        model = Khedmat
        field = '__all__'

    