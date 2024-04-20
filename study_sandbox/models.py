from django.db import models

from courses.models import LessonContent
from authorization.models import User

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    lesson_content = models.ForeignKey(LessonContent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_questions(self):
        return self.qustion_set.all()
    
    class Meta:
        verbose_name_plural = 'Quizes'
    
    
class Question(models.Model):
    text = models.CharField(max_length=300)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.text)
    
    def get_answers(self):
        return self.answer_set.all()
    

class Answer(models.Model):
    text = models.CharField(max_length=300)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.text)
    
    
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self) -> str:
        return str(self.pk)
    