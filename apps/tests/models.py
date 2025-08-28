from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Test(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, related_name="questions", 
                             on_delete=models.CASCADE)
    text = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", 
                                 on_delete=models.CASCADE)
    text = models.CharField(max_length=255) 
    is_correct = models.BooleanField(default=False) 

    def __str__(self):
        return self.text


class UserResult(models.Model):
    user = models.ForeignKey(User, related_name="results", on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name="results", on_delete=models.CASCADE)
    score = models.IntegerField(default=0) 
    taken_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test.title} - {self.score}"
