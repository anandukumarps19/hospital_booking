from django.contrib import admin
from .models import Department, Doctors, Booking

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)


class Bookingadmin(admin.ModelAdmin):
    list_display=('id','name','email','Doctor_name','date','Booked_on')

admin.site.register(Booking,Bookingadmin)