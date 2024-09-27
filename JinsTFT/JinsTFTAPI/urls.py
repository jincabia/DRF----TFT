from django.urls import path
from .views import *

urlpatterns = [
    path('recent/', RecentMatchView.as_view()),
    path('recent/<str:match_id>/', CheckMatchView.as_view()),
    path('games/', GameModelView.as_view()),
    path('games/<str:gameID>', GameInfoView.as_view()),
    path('tactician-placement/<str:item_id>', TacticianPlacementView.as_view()),
    path('most-played-tactician/',MostUsedTactician.as_view()),
    path('tacticians/', TacticianModelView.as_view()),
    path('game-ids/', GameIdView.as_view()),



]