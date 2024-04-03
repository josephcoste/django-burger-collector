from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feeding 
from .models import Burger
from .serializers import FeedingSerializer
from rest_framework import generics
from .serializers import BurgerSerializer
from .serializers import HappymealSerializer
from .models import Happymeal
# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the burger-collector api home route!'}
    return Response(content)

class FeedingListCreate(generics.ListCreateAPIView):
  serializer_class = FeedingSerializer

  def get_queryset(self):
    burgers_id = self.kwargs['burgers_id']
    return Feeding.objects.filter(burgers_id=burgers_id)

  def perform_create(self, serializer):
    burgers_id = self.kwargs['burgers_id']
    burgers = Burger.objects.get(id=burgers_id)
    serializer.save(burgers=burgers)

class FeedingDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = FeedingSerializer
  lookup_field = 'id'

  def get_queryset(self):
    burgers_id = self.kwargs['burgers_id']
    return Feeding.objects.filter(burgers_id=burgers_id)


class BurgerList(generics.ListCreateAPIView):
  queryset = Burger.objects.all()
  serializer_class = BurgerSerializer

class BurgerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Burger.objects.all()
  serializer_class = BurgerSerializer
  lookup_field = 'id'

class HappymealDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Happymeal.objects.all()
  serializer_class = HappymealSerializer
  lookup_field = 'id'

class HappymealList(generics.ListCreateAPIView):
  queryset = Happymeal.objects.all()
  serializer_class = HappymealSerializer