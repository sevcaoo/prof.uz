from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
class Button(BaseModel):
    name=models.CharField(max_length=100)
    link=models.URLField()
    

from django.db import models

class Profession(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:30]


class Training(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in hours")

    def __str__(self):
        return self.name


    def __str__(self):
        return self.title
