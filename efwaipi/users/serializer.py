from blog.models import *
from rest_framework import serializers

class VacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaksinasi
        fields = '__all__'
        print("*****************masuk serializer")