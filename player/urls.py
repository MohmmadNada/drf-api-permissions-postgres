# from django.contrib import admin
from django.urls import path,include
from .views import PlayersListView,PlayersDetailsView
urlpatterns = [
    path('',PlayersListView.as_view(),name='player_list_api'),
    path('<int:pk>/',PlayersDetailsView.as_view(),name='player_detail_api'),
]