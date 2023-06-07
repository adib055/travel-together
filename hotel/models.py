from django.db import models
from traveller.models import traveller

# Create your models here.

#8.	Hotel (hotel_id, hotel_name, hotel_location, hotel_star, place_id)
class hotel(models.Model):
    hotel_id=models.CharField(max_length=50)
    hotel_name=models.CharField(max_length=50)
    hotel_location=models.CharField(max_length=50)
    hotel_star=models.FloatField()



#9.	Room Information (room_num, room_type,  price, hotel.id

class roominformation(models.Model):
    room_num=models.CharField(max_length=50)
    room_type=models.CharField(max_length=50)
    price=models.IntegerField()
    #user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hotel=models.ForeignKey(hotel, on_delete=models.CASCADE, null=True)

#10.	Reservation(reservation_id, Traveller.id, room_num, reservation_date, date_in, date_out, payment)
class reservation(models.Model):
    reservation_id=models.IntegerField()
    traveller = models.ForeignKey(traveller, on_delete=models.CASCADE)
    roominformation=models.ForeignKey(roominformation, on_delete=models.CASCADE, null=True)
    reservation_date=models.DateField()
    date_in=models.DateField()
    date_out=models.DateField()
    payment=models.IntegerField()

#11.	HotelTranssaction(transaction_id, reservation_id, transaction_date)

class hoteltransaction(models.Model):
    transaction_id=models.IntegerField()
    reservation=models.ForeignKey(reservation, on_delete=models.CASCADE,null=True)
    transaction_date=models.DateField()

