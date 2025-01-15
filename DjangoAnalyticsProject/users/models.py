from django.contrib.auth.models import AbstractUser
from django.db import models


# Переопределяем пользователя
class User(AbstractUser):
    pass

