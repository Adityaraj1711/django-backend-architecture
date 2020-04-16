from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ serializes a name for testing our api """
    name = serializers.CharField(max_length=10)

