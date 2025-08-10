from django.shortcuts import redirect
from django.urls import reverse


class QuizLockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        active_quiz_id = request.session.get('active_quiz_id')

        if active_quiz_id:

            allowed_paths = [
                reverse('quiz:start', args=[active_quiz_id]),
            ]

            if request.method == "POST" and request.path in allowed_paths:
                return self.get_response(request)

            if request.path not in allowed_paths:
                return redirect('quiz:start', active_quiz_id)

        return self.get_response(request)
