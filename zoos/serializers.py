from .models import Zoo
from rest_framework import serializers

class ZooSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Which model will get serialized by this class
        model = Zoo
        # Which fields should be included in the output
        fields = ['id', 'subject', 'details', 'info']