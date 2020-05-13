from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing the api view"""
    name = serializers.CharField(max_length=10)
