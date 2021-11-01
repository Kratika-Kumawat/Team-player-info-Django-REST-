from rest_framework import routers, viewsets ,serializers
from .models import Teams
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'
        