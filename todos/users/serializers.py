from rest_framework import serializers

from .models import CustomUser
 

class BriefCustomUserSerializer(serializers.ModelSerializer):
 
    class Meta(object):
        model = CustomUser
        fields = ('usernamec', 'logo')
        extra_kwargs = {'password': {'write_only': True}}

 
class FullCustomUserSerializer(serializers.ModelSerializer):
 
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = CustomUser
        fields = ('id', 'email', 'usernamec', 'bio',
                  'date_joined', 'logo','password', 'firstname', 'lastname')
        extra_kwargs = {'password': {'write_only': True}}