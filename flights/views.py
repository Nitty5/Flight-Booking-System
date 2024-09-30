from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Flight, Ticket

from .serializers import FlightSerializer, TicketSerializer


class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightSearchView(generics.ListAPIView):
    serializer_class = FlightSerializer

    def get_queryset(self):
        departure_city = self.request.query_params.get('departure_city', None)
        destination_city = self.request.query_params.get('destination_city', None)
        date = self.request.query_params.get('date', None)

        queryset = Flight.objects.all()
        if departure_city:
            queryset = queryset.filter(departure_city=departure_city)
        if destination_city:
            queryset = queryset.filter(destination_city=destination_city)
        if date:
            queryset = queryset.filter(departure_time__date=date)
        return queryset

class BookFlightView(generics.CreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        flight = serializer.validated_data['flight']
        seat_number = serializer.validated_data['seat_number']

        if Ticket.objects.filter(flight=flight, seat_number=seat_number).exists():
            raise serializer.ValidationError("Seat already booked!")
        serializer.save(user=self.request.user)

class UserPastBookingsView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)
