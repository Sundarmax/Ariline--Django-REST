from django.contrib import admin
from .models import flight,flight_details,passenger_info,ticket_info,card_details

# Register your models here.
admin.site.register(flight)
admin.site.register(flight_details)
admin.site.register(ticket_info)
admin.site.register(passenger_info)
admin.site.register(card_details)

