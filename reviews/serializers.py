

from rest_framework import serializers
from  .models import Contributor 
from .models import Book, Publisher

# class PublisherSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     website = serializers.URLField()
#     email = serializers.EmailField()
    
    
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     publication_date = serializers.DateField()
#     isnb = serializers.CharField()
#     publisher = PublisherSerializer()
    

class ContributorSerializer(serializers.ModelSerializer()):
    
    class Meta:
        model = Contributor
        fields = ["first_names","last_names","email"]
        

class PublisherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = ['name','website', 'email']
        
        
class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    
    class Meta:
        model = Book
        fields = ['title','publication_date', 'isnb']