from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
class Button(BaseModel):
    name=models.CharField(max_length=100)
    link=models.URLField()