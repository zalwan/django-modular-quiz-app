import nested_admin
from django.contrib import admin

# Register your models here.
from django.core.exceptions import ValidationError
from .models import Quiz, Question, Choice, Answer, QuizAttempt


class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 2


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]


@admin.register(Quiz)
class QuizAdmin(nested_admin.NestedModelAdmin):
    list_display = ("title", "description")
    inlines = [QuestionInline]

    def save_model(self, request, obj, form, change):
        """Override save_model to set user to request.user"""
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        """
        rules:
        - Only one Choice can be correct
        - There must be at least one correct Choice
        """
        super().save_related(request, form, formsets, change)
        quiz = form.instance
        for question in quiz.questions.all():
            correct_choices = question.choices.filter(is_correct=True).count()
            if correct_choices == 0:
                raise ValidationError(
                    f"Questions '{question.text}' must have at least one correct choice."
                )


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "quiz", "score", "date_taken")
    list_filter = ("quiz", "user")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("attempt", "question", "choice")
    list_filter = ("question",)
