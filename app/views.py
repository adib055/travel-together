
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib import messages
from hotel.models import *
from car.models import*
from .forms import RegistrationForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile_submit(request):
    return render(request, 'profile_form_submit.html')

def findroute(request):
    return render(request, 'findroute.html')

def route(request):
    return render(request, 'route.html')

def carentals(request):
    return render(request, 'carentals.html')

def booking(request):
    return render(request, 'booking.html')

def profile(request):
    return render(request, 'profile.html')

def history(request):
    return render(request, 'history.html')

# def login(request):
#      return render(request, 'login.html')

# def LogoutView(request):
#     LOGOUT(request)
#     return redirect('login')

#def registration(request):
#    fm=UserCreationForm()
#    return render(request, 'registration.html',{'form':fm})

class RegistrationView(View):
    def get(self, request): 
        form = RegistrationForm()
        return render(request, 'registration.html',{'form':form})
    def post(self,request):
        form = RegistrationForm(request.POST)
        messages.success(request, 'Congratulations! Registered Succesfully')
        if form.is_valid():
            form.save()
        return render(request, 'registration.html',{'form':form})



#def test(request):
#    hotel1=hotel(hotel_id=1112,hotel_name='Marriott',hotel_location='sajek',
#                hotel_star=3.8)
#    hotel1.save()

 #   roominformation1=roominformation(room_num='503',room_type='5 star',price=3000)
 #   roominformation1.save()

 #   reservation1=reservation(reservation_id=1212,reservation_date='2023-10-25',date_in='2006-10-25',date_out='2006-10-25',payment=3000
  #                           , roominformation = roominformation.objects.get(room_num=503))
   # reservation1.save()
    #roominformation=models.ForeignKey(roominformation, on_delete=models.CASCADE, null=True)

#    hoteltransaction1=hoteltransaction(transaction_id=1123,transaction_date='2023-10-25')
    #reservation=models.ForeignKey(reservation, on_delete=models.CASCADE,null=True)

 #   car1=car(car_id='8688',car_number='t-1202',rent_price=4500)
  #  car1.save()
    #driver=models.ForeignKey(driver, on_delete=models.CASCADE, null=True)
   # driver1=driver(driver_id='aj12',nid='12344161616')
   # driver1.save()

    
    #return render(request, 'home.html')

