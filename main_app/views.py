from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feeding 
from .models import Burger
from .serializers import FeedingSerializer
from rest_framework import generics
from .serializers import BurgerSerializer
from .serializers import HappymealSerializer
from .models import Happymeal
from rest_framework import generics, status, permissions 
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer, BurgerSerializer
from rest_framework.exceptions import PermissionDenied

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
  permission_classes = [permissions.IsAuthenticated]

def get_queryset(self):
      # This ensures we only return cats belonging to the logged-in user
      user = self.request.user
      return Burger.objects.filter(user=user)

def perform_create(self, serializer):
      # This associates the newly created cat with the logged-in user
      serializer.save(user=self.request.user)


class BurgerDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = BurgerSerializer
  lookup_field = 'id'

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)


    happymeal_not_associated = Happymeal.objects.exclude(id__in=instance.toys.all())
    happymeal_serializer = HappymealSerializer(happymeal_not_associated, many=True)

    return Response({
        'burgers': serializer.data,
        'happymeal_not_associated': happymeal_serializer.data
    })
def perform_update(self, serializer):
    burger = self.get_object()
    if burger.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to edit this burger."})
    serializer.save()

def perform_destroy(self, instance):
    if instance.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to delete this burger."})
    instance.delete()


class HappymealDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Happymeal.objects.all()
  serializer_class = HappymealSerializer
  lookup_field = 'id'

class HappymealList(generics.ListCreateAPIView):
  queryset = Happymeal.objects.all()
  serializer_class = HappymealSerializer

class AddHappymealToBurger(APIView):
  def post(self, request, burgers_id, happymeal_id):
    burger = Burger.objects.get(id=burgers_id)
    happymeal = Happymeal.objects.get(id=happymeal_id)
    burger.happymeal.add(happymeal)
    return Response({'message': f'Happymeal {happymeal.name} added to Burger {happymeal.name}'})
  
class RemoveHappymealFromBurger(APIView):
  def post(self, request, burgers_id, happymeal_id):
    burger = Burger.objects.get(id=burgers_id)
    happymeal = Happymeal.objects.get(id=happymeal_id)
    burger.happymeal.remove(happymeal)
    return Response({'message': f'Happymeal {happymeal.name} removed from Burger {happymeal.name}'})

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self,request,*args,**kwargs):
    response = super().create(request,*args,**kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })
  
class LoginView(APIView):
 permission_classes = [permissions.AllowAny]

class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })
def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
