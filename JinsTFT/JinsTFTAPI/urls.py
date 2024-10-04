from django.urls import path
from .views import *

urlpatterns = [
    path('recent/', RecentMatchView.as_view()),
    path('recent/<str:match_id>/', CheckMatchView.as_view()),
    path('games/', GameIdView.as_view()),
    path('games/<str:gameID>', GameInfoView.as_view()),
    path('tactician-placement/<str:item_id>', TacticianPlacementView.as_view()),
    path('most-played-tactician/',MostUsedTactician.as_view()),
    path('tacticians/', TacticianModelView.as_view()),
    path('game-ids/', GameIdView.as_view()),
    path('static-units/', StaticUnitView.as_view()),
    path('dynamic-units/', DynamicUnitView.as_view()),
    # path('populate-units/', PopulateUnitView.as_view()),
    path('populate-tact/', PopulateTacticians.as_view()),

    path('popular-units/', MostUsedUnitView.as_view()),

    

]


