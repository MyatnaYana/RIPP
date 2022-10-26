from django.contrib import admin

# Register your models here.
from .models import Mins, Address, Customer, Reservation

admin.site.register(Mins)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Reservation)
