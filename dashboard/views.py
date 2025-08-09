from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    # sample data
    quizzes = [
        {"id": 1, "title": "Python Basics",
            "description": "Test your Python knowledge"},
        {"id": 2, "title": "Django Fundamentals",
            "description": "How well do you know Django?"},
    ]
    attempts = [
        {"quiz_title": "Python Basics", "score": 80},
        {"quiz_title": "Django Fundamentals", "score": 90},
    ]
    context = {
        "quizzes": quizzes,
        "attempts": attempts
    }
    return render(request, "dashboard/index.html", context)
