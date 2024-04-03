from django.urls import path
from .views import Home , BurgerList, BurgerDetail , FeedingListCreate,FeedingDetail, HappymealDetail, HappymealList

urlpatterns = [
path('', Home.as_view(), name='home'),
path('burgers/', BurgerList.as_view(), name='burger-list'),
path('burgers/<int:id>/', BurgerDetail.as_view(), name='burger-detail'),
path('burgers/<int:burgers_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
path('burgers/<int:burgers_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
path('burgers/<int:id>/', HappymealDetail.as_view(), name='happymeal-detail'),
path('burgers/', HappymealList.as_view(), name='happymeal-list'),
]
