from django.contrib import admin

# Register your models here.

class car(admin.ModelAdmin):
    fields = ["driver_id", "nid"]
