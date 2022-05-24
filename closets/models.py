from django.db import models
from user.models import User

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name

class Closet(models.Model):
      SPRING = 1
      SUMMER = 2
      FALL = 3
      WINTER = 4

      SEASONS_CHLICES = [(SPRING, '봄'),
                         (SUMMER, '여름'),
                         (FALL, '가을'),
                         (WINTER, '겨울')]
      id = models.AutoField(primary_key=True)
      cname = models.CharField(max_length=200)
      photo = models.ImageField(blank=False)
      detail = models.TextField()
      user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

      def __str__(self):
          return self.cname

