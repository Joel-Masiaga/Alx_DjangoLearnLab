from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  # Display the actor as a string (username)
    target_content_type = serializers.StringRelatedField()  # Display the content type as a string (e.g., 'post')

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target_content_type', 'target_object_id', 'timestamp', 'read']
        read_only_fields = ['id', 'recipient', 'actor', 'verb', 'target_content_type', 'target_object_id', 'timestamp', 'read']
