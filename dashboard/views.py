from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from quiz.models import Quiz, QuizAttempt


@login_required
def index(request):
    quizzes = Quiz.objects.all()
    attempts = QuizAttempt.objects.filter(user=request.user)

    # Only show report to admins
    report = None
    if request.user.is_staff:
        report = (
            QuizAttempt.objects
            .select_related("user", "quiz")
            .all()
        )

    return render(
        request,
        "dashboard/index.html",
        {
            "quizzes": quizzes,
            "attempts": attempts,
            "report": report,
        },
    )


@login_required
def delete_attempt(request, attempt_id):
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user)
    if request.method == "POST":
        attempt.delete()
        return redirect('dashboard:index')
    return redirect('dashboard:index')


@login_required
def delete_all_history(request):
    if request.method == "POST":
        QuizAttempt.objects.filter(user=request.user).delete()
    return redirect('dashboard:index')
