from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('chat/<int:chat>/get_message/<int:pk>/', views.MessageView.as_view(), name=views.MessageView.name),

    path('chat/<int:chat>/get_last_messages/<int:quantity>/', views.MessageListView.as_view(), name=views.MessageListView.name),
    path('chat/<int:chat>/get_last_messages/', views.MessageFixedListView.as_view(), name=views.MessageFixedListView.name),
    path('chat/<int:chat>/create_message/', views.MessageCreationView.as_view(), name=views.MessageCreationView.name),
    path('chat/create_private/', views.PrivateChatCreationView.as_view(), name=views.PrivateChatCreationView.name),
    path('chat/create_public/', views.RoomCreationView.as_view(), name=views.RoomCreationView.name),
    path('token/get/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', views.UserCreationView.as_view(), name=views.UserCreationView.name),
]
