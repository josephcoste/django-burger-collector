from django.urls import path
from .views import Home , BurgerList, BurgerDetail , FeedingListCreate,FeedingDetail, HappymealDetail, HappymealList ,AddHappymealToBurger,RemoveHappymealFromBurger,CreateUserView,LoginView,VerifyUserView

urlpatterns = [
path('', Home.as_view(), name='home'),
path('burgers/', BurgerList.as_view(), name='burger-list'),
path('burgers/<int:id>/', BurgerDetail.as_view(), name='burger-detail'),
path('burgers/<int:burgers_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
path('burgers/<int:burgers_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
path('burgers/<int:id>/', HappymealDetail.as_view(), name='happymeal-detail'),
path('burgers/', HappymealList.as_view(), name='happymeal-list'),
path('burgers/<int:burgers_id>/add_happymeal/<int:happymeal_id>/', AddHappymealToBurger.as_view(), name='add-happymeal-to-burgers'),
path('burgers/<int:burgers_id>/remove_happymeal/<int:happymeal_id>/', RemoveHappymealFromBurger.as_view(), name='remove-happymeal-from-burgers'),
path('users/register/', CreateUserView.as_view(), name='register'),
path('users/login/', LoginView.as_view(), name='login'),
path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),


]
