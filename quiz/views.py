from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Choice, QuizAttempt, Answer


@login_required
def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.questions.all()

    # Set lock quiz ke session
    if request.method == "GET":
        request.session['active_quiz_id'] = quiz.id

    if request.method == "POST":
        score = 0
        attempt = QuizAttempt.objects.create(
            user=request.user, quiz=quiz, score=0
        )
        for question in questions:
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = Choice.objects.get(pk=choice_id)
                Answer.objects.create(
                    attempt=attempt, question=question, choice=choice
                )
                if choice.is_correct:
                    score += 1
        final_score = (score / questions.count()) * \
            100 if questions.count() > 0 else 0
        attempt.score = final_score
        attempt.save()

        # unlock quiz
        if 'active_quiz_id' in request.session:
            del request.session['active_quiz_id']

        return redirect('quiz:result', attempt_id=attempt.id)

    return render(request, "quiz/start.html", {"quiz": quiz, "questions": questions})


@login_required
def result(request, attempt_id):
    attempt = get_object_or_404(QuizAttempt, pk=attempt_id, user=request.user)
    return render(request, "quiz/result.html", {"attempt": attempt})
