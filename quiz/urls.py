from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
    path('<int:quiz_id>/', views.start_quiz, name='start'),
    path('result/<int:attempt_id>/', views.result, name='result'),
]
