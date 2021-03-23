from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Info(models.Model):
    client = models.CharField('客户端', max_length=20,unique=True)
    score = models.IntegerField('分数', default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client,self.score}'