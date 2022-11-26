from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('menu/', views.Menu.as_view(), name='menu'),
    # path(
    #     'manage_bookings/',
    #     views.ListBookingView.as_view(), name='manage_bookings'),
    path('thank_you/', views.ThankYou.as_view(), name='thank_you'),
    path('update_booking/', views.ListBookingView.as_view(), name='update_booking'),
    path('manage_bookings/<booking_id>', views.edit_booking_view, name='edit'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete'),
]
