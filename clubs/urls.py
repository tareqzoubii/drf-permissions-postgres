from django.urls import path
from .views import ClubsListView,ClubsDetailView,PlayersListView,PlayersDetailView
# Create your urls here.

urlpatterns = [
   path('clubs/', ClubsListView.as_view(), name='clubs_list'),
   path('clubs/<int:pk>', ClubsDetailView.as_view(),name='clubs_detail'),
   path('players/', PlayersListView.as_view(), name='players_list'),
   path('players/<int:pk>', PlayersDetailView.as_view(),name='players_detail')
]