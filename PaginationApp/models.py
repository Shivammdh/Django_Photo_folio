from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name=models.CharField(max_length=200)
    user_designation=models.CharField(max_length=200)
    user_description=models.CharField(max_length=5000)

    def __str__(self):
        return self.user_name