from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def chat_view(request):
    if request.method == 'POST':
        user = request.user
        title = request.data.get('title', 'New Conversation')

        conversation = Conversation.objects.create(user=user, title=title)

        message_content = request.data.get('content', '')
        Message.objects.create(conversation=conversation, role='user', content=message_content)

        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def conversation_list_view(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return Response({"error": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        conversations = Conversation.objects.filter(user=request.user)
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def conversation_detail_view(request, id):
    try:
        conversation = Conversation.objects.get(id=id, user=request.user)
    except Conversation.DoesNotExist:
        return Response({"error": "Conversation not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)