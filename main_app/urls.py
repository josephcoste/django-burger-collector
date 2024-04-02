from django.urls import path
from .views import Home ,BurgerList, BurgerDetail

urlpatterns = [
path('', Home.as_view(), name='home'),
path('burgers/', BurgerList.as_view(), name='burger-list'),
path('burgers/<int:id>/', BurgerDetail.as_view(), name='burger-detail'),
]
