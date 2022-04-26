from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
import uuid
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    AUTH_NORMAL_USER = 0
    AUTH_BRAND_ADMIN = 1
    AUTH_CHOICES = [
        (AUTH_NORMAL_USER, '일반 사용자'),
        (AUTH_BRAND_ADMIN, '브랜드 관리자'),
    ]

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True,
                          serialize=True)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'ID',
        max_length=150,
        unique=True,
        help_text='150자 이내, 영문자, 숫자, @/./+/-/_ 만 사용 가능',
        validators=[username_validator],
        error_messages={
        'unique': "이미 존재하는 ID 입니다.",
    },
    )
    email = models.EmailField(blank=False, null=False)
    nickname = models.CharField(blank=False, null=False, max_length=100)
    auth = models.IntegerField(choices=AUTH_CHOICES,
                               blank=False,
                               null=False,
                               default=0
                               )
    REQUIRED_FIELDS = ['nickname', 'email', 'auth']
