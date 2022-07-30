from rest_framework.serializers import ModelSerializer
from base.models import Friend
from base.models import Chat
from django.contrib.auth.models import User

class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        
class FriendSerializer(ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'