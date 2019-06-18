from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('chat/<int:chat>/messages/', views.MessageFixedList.as_view(), name=views.MessageFixedList.name),
    path('chat/<int:chat>/messages/<int:quantity>/', views.MessageList.as_view(), name=views.MessageList.name),
    path('chat/<int:chat>/message/', views.MessageCreation.as_view(), name=views.MessageCreation.name),
    path('chat/<int:chat>/message/<int:pk>/', views.MessageView.as_view(), name=views.MessageView.name),
    path('chat/private/', views.PrivateChatView.as_view(), name=views.PrivateChatView.name),
    path('room/', views.RoomView.as_view(), name=views.RoomView.name),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
