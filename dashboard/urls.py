from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.index, name='index'),
    path('delete-history/', views.delete_all_history, name='delete_all_history'),
    path('delete-attempt/<int:attempt_id>/',
         views.delete_attempt, name='delete_attempt'),

]
