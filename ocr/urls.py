from django.urls import path
from .views import OCR

urlpatterns = [
    path("", OCR.as_view()),
]