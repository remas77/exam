from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),  # مسار للبحث
    path('add/', views.add_member, name='add_member'),  # مسار لإضافة البيانات
    path('list/', views.list_members, name='list_members'),
    path('delete/<int:member_id>/', views.delete_member, name='delete_member'),
    path('home/', views.home, name='home'),
    path('games/', views.list_games, name='list_games'),
    path('add2/', views.add_game, name='add_game'),
    path('edit/<int:game_id>/', views.edit_game, name='edit_game'),
    path('delete/<int:game_id>/', views.delete_game, name='delete_game'),
    path('search2/', views.search_games, name='search_games'),
]
