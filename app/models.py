from django.db import models
from django.core.exceptions import ValidationError
#from django.forms import ValidationError
# Create your models here.
def check_for_k(value):
    if value[0].lower()=='k':
        raise ValidationError('started with k')



class Topic(models.Model):
    topic_name=models.CharField(max_length=100,validators=[check_for_k])

    def __str__(self):
        return self.topic_name