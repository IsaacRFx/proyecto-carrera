from django.contrib.auth.models import UserManager
from rest_framework import serializers

from api.models import KuderTest, LearningTypeTest, TechUser


class KuderTestSerializer(serializers.ModelSerializer):
    result_pretty = serializers.SerializerMethodField(read_only=True) 

    class Meta:
        model = KuderTest
        fields = '__all__'

    def get_result_pretty(self, obj):
        return obj.get_result_display()

class LearningTypeSerializer(serializers.ModelSerializer):
    result_pretty = serializers.SerializerMethodField(read_only=True) 

    class Meta:
        model = LearningTypeTest
        fields = '__all__'

    def get_result_pretty(self, obj):
        return obj.get_result_display()

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechUser
        fields = '__all__'
