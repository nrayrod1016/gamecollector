from django.urls import path 
from . import views 

urlpatterns = [ 
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about' ), 
  path('games/', views.games_index, name='games_index'), 
  path('games/<int:game_id>/', views.games_detail, name='games_detail'),
  path('games/create/', views.GameCreate.as_view(), name='games_create'), 
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
  path('games/<int:game_id>/add_playing/', views.add_playing, name='add_playing'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('games/<int:game_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('accounts/signup/', views.signup, name='signup'),
]


