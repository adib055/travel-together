from django.shortcuts import render

# Create your views here.

def hotel_view(request):

    return render(request,'base.html')
