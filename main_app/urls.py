from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('accounts/signup/', views.signup, name='signup'),
    path('chats/', views.chats_index, name="index"),
    path('chats/<int:pk>/delete/', views.ChatDelete.as_view(), name='chats_delete'),
    path('chats/create/', views.ChatCreate.as_view(), name='chats_create'),
    path('chats/<int:pk>/', views.ChatDetail.as_view(), name="chats_detail"),
    path('chats/<int:pk>/update/', views.ChatUpdate.as_view(), name="chats_update"),
]
