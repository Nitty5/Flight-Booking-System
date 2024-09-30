from django.urls import path
from .views import FlightListView, FlightSearchView, BookFlightView, UserPastBookingsView

urlpatterns = [
    path('flights/', FlightListView.as_view(), name='flight-list'),
    path('flights/search/', FlightSearchView.as_view(), name='flight-search'),
    path('flights/book/', BookFlightView.as_view(), name='book-flight'),
    path('past/bookings/', UserPastBookingsView.as_view(), name='user-bookings'),
]
