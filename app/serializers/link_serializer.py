from rest_framework import serializers

class LinkSerializer(serializers.Serializer):
    institution = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
