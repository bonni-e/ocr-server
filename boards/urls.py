from django.urls import path
from .views import Boards, BoardDetail

urlpatterns = [
    path('', Boards.as_view()),
    path('board/<int:pk>', BoardDetail.as_view()),
]