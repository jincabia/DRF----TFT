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
    path('populate-trait/', PopulateTraits.as_view()),
    path('populate-placement/', PopulateGamePlacements.as_view()),

    path('popular-units/', MostUsedUnitView.as_view()),
    path('view-static-traits/', StaticTraitViewSet.as_view({'get': 'list'})),
    path('view-dynamic-traits/', DynamicTraitViewSet.as_view({'get': 'list'})),
    path('popular-traits/', MostPlayedDynamicTraitViewSet.as_view({'get': 'list'})),
    path('view-placements/', GamePlacementView.as_view()),
    
    path('find-game/<str:game>', FindGame.as_view()),


]


