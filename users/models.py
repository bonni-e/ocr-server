from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser) :
    # 상속 받은 필드 사용 안함 
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)

    # 나만의 필드 추가 
    name = models.CharField(max_length=40, default="")

    def board_count(self) :
        return self.boards.count()
