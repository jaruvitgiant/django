from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=500)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.correct else 'Incorrect'})"