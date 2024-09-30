from django.contrib import admin
from .models import Flight, Ticket


class FlightAdmin(admin.ModelAdmin):
    list_display = ('airline', 'flight_number', 'departure_city', 'destination_city', 'departure_time', 'arrival_time', 'price')
    search_fields = ('airline', 'flight_number', 'departure_city', 'destination_city')
    list_filter = ('departure_city', 'destination_city', 'departure_time')

class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'seat_number', 'booking_status')
    search_fields = ('user__username', 'flight__flight_number', 'seat_number')
    list_filter = ('booking_status',)

admin.site.register(Flight, FlightAdmin)
admin.site.register(Ticket, TicketAdmin)
