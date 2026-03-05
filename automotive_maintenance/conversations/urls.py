from django.urls import path
from . import views

urlpatterns = [
    path('conversation/', views.chat_view, name='chat_view'),
    path('conversations/', views.conversation_list_view, name='conversation_list'),
    path('conversations/<int:id>/', views.conversation_detail_view, name='conversation_detail'),
]