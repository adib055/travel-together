from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#4.	Driver ( driver_id , …, photo, nid, User.id)
class driver(models.Model):
    driver_id=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='./userprofile/')
    nid=models.CharField(max_length=15)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)



#5.	Car (car_id, car_number, rent_price, driver_id)

class car(models.Model):
    car_id=models.CharField(max_length=6)
    car_number=models.CharField(max_length=15)
    rent_price=models.IntegerField()
    driver=models.ForeignKey(driver, on_delete=models.CASCADE, null=True)

#6.	CarRentals (rental_id, Car.id, Traveller.id, rent_date, arrive_time, Place.place_id, date_return, payment_amount)
class carrentals(models.Model):
    rental_id=models.CharField(max_length=15)
    car=models.ForeignKey(car,on_delete=models.CASCADE, null=True)
    #traveller_id
    rent_date=models.DateField()
    arrive_time=models.TimeField()
    #placeid
    date_return=models.DateField()
    payment_amount=models.IntegerField()

#7.	CarTansaction (trans_id, rental_id, trans_date)
class cartransaction(models.Model):
    trans_id=models.CharField(max_length=50)
    carrentals=models.ForeignKey(carrentals,on_delete=models.CASCADE,null=True)
    tras_date=models.DateField()