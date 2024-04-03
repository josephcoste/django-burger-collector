from rest_framework import serializers
from .models import Burger
from rest_framework import generics
from .models import Burger
from .models import Feeding 
from .models import Happymeal

class FeedingSerializer(serializers.ModelSerializer):
   class Meta:
      model= Feeding
      fields='_all_'
      read_only_fields = ('burgers',)

class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = '__all__'

def get_fed_for_today(self, obj):
    return obj.fed_for_today()

class HappymealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Happymeal
        fields = '_all_'
        