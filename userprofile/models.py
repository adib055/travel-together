from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#2.	Admin (admin_id, date_of_birth, photo, User.id)

class userprofile(models.Model):
    admin_id=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='./userprofile/')
    date_of_birth=models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
