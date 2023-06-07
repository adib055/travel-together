from django.contrib import admin
from django.urls import path,include
admin.site.site_header = "App Admin"
admin.site.site_title = "Booking for Travel Admin Portal"
admin.site.index_title = "Welcome to Booking for Travel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')), #Reverse for 'password reset' not found. 'password reset' is not a valid view function or pattern name.
    path('',include('app.urls')),
]
