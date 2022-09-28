from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Todo(models.Model):
    # django 에서 pk는 자동으로 만들어준다.
    content = models.CharField(max_length=80)

    """
    defalut : 
    데이터를 생성할 때 값을 안넣으면 
    자동으로 값을 채워서 데이터를 생성
    """
    completed = models.BooleanField(default=False)
