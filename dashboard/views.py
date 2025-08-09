from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from quiz.models import Quiz, QuizAttempt


@login_required
def index(request):
    quizzes = Quiz.objects.all()
    attempts = QuizAttempt.objects.filter(user=request.user)
    return render(request, "dashboard/index.html", {"quizzes": quizzes, "attempts": attempts})
