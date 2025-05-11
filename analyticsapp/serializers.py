from rest_framework import serializers
from .models import UserActivity

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ['site', 'user', 'visitor_id', 'event_type', 'description', 'page_url', 'user_agent', 'ip_address', 'timestamp']


