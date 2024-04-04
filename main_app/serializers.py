from rest_framework import serializers
from .models import Burger
from rest_framework import generics
from .models import Burger
from .models import Feeding 
from .models import Happymeal
from django.contrib.auth.models import User

class FeedingSerializer(serializers.ModelSerializer):
   class Meta:
      model= Feeding
      fields='_all_'
      read_only_fields = ('burgers',)


class HappymealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Happymeal
        fields = '_all_'

class BurgerSerializer(serializers.ModelSerializer):
    happymeal = HappymealSerializer(many=True, read_only=True) 
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    model = Burger
    fields = '__all__'
def get_fed_for_today(self, obj):
    return obj.fed_for_today()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user