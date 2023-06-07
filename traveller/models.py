from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#3.	Traveller (id, gender, date_of_birth, photo, User.id)

class traveller(models.Model):
    gender=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
