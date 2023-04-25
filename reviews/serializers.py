

from rest_framework import serializers
from  .models import Contributor

class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField()
    website = serializers.URLField()
    email = serializers.EmailField()
    
    
class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    publication_date = serializers.DateField()
    isnb = serializers.CharField()
    publisher = PublisherSerializer()
    
