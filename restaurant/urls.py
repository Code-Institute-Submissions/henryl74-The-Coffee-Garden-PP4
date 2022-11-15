# URLs for the site

from . import views
from django.urls import path


app_name = 'restaurant'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('menu/', views.Menus.as_view(), name='menu'),
    # path('thank_you/', views.ThankYou.as_view(), name='thank_you'),
    # path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path(
        'manage_bookings/',
        views.ListBookingView.as_view(), name='manage_bookings'),
    path(
        'update_booking/<booking_id>',
        views.update_booking_view, name='update'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete'),
]
