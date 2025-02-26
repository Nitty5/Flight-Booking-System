from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.airline} - {self.flight_number}'

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    booking_status = models.CharField(max_length=20, default='Confirmed')

    def __str__(self):
        return f'{self.user.username} - {self.flight.flight_number} - {self.seat_number}'
