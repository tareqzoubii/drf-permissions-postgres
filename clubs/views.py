from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import ClubsSerializer,PlayerSerializer
from .models import Clubs,Players
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class ClubsListView(ListCreateAPIView):
    queryset=Clubs.objects.all()
    serializer_class= ClubsSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    

class ClubsDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Clubs.objects.all()
    serializer_class= ClubsSerializer
    permission_classes=[IsOwnerOrReadOnly]

class PlayersListView(ListCreateAPIView):
    queryset=Players.objects.all()
    serializer_class= PlayerSerializer
    permission_classes=[AllowAny]


class PlayersDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Players.objects.all()
    serializer_class= PlayerSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]