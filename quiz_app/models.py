# Create your models here.
from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=255)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    # def __str__(self):
    #     return f"{self.text} ({'Correct' if self.correct else 'Incorrect'})"

    # class Meta:
    #     # Ensures that for a given question, there's only one correct choice
    #     # You might adjust this based on your specific quiz logic (e.g., multiple correct answers)
    #     unique_together = ('question', 'correct')
    #     constraints = [
    #         models.UniqueConstraint(fields=['question'], condition=models.Q(correct=True), name='unique_correct_choice')
    #     ]
