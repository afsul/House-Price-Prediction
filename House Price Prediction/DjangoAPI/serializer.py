from rest_framework import serializers 
from .models import Houses 

class HousesSerializers(serializers.ModelSerializer): 
    class meta: 
        model=Houses 
        fields='__all__'