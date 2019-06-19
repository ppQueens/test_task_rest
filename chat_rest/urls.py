from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('chat/<int:chat>/messages/', views.MessageFixedListView.as_view(), name=views.MessageFixedListView.name),
    path('chat/<int:chat>/messages/<int:quantity>/', views.MessageListView.as_view(), name=views.MessageListView.name),
    path('chat/<int:chat>/message/', views.MessageCreationView.as_view(), name=views.MessageCreationView.name),
    path('chat/<int:chat>/message/<int:pk>/', views.MessageView.as_view(), name=views.MessageView.name),
    path('chat/private/<int:user_1>/<int:user_2>/', views.PrivateChatCreationView.as_view(), name=views.PrivateChatCreationView.name),
    path('room/', views.RoomCreationView.as_view(), name=views.RoomCreationView.name),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', views.UserCreationView.as_view(), name=views.UserCreationView.name),
]
