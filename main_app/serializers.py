from rest_framework import serializers
from .models import Burger
from rest_framework import generics
from .models import Burger
from .serializers import BurgerSerializer


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = '__all__'
class BurgerList(generics.ListCreateAPIView):
  queryset = Burger.objects.all()
  serializer_class = BurgerSerializer

class BurgerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Burger.objects.all()
  serializer_class = BurgerSerializer
  lookup_field = 'id'