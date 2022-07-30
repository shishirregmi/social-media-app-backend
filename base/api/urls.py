from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('',views.getRoutes),
    path('chats/add', views.addChats),
    path('user/add', views.addUsers),
    path('friends/', views.getFriends),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('chats/<str:room>', views.getChats),
]
