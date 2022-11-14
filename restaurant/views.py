from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Booking
from .forms import BookingForm
from django.contrib import messages

# Create your views here.


def home(request):
    """The view for the start page. Renders the index.html
    page which also extends the base.html
    """
    return render(request, 'index.html')


def booking_page(request):
    """The view for the booking page. If user is logged in it renders the
    booking.html, otherwise it renders the page to login or signup.
    When user has made a booking it redirects to mybooking overview page.
    It takes the input from the form and store it in the Booking model.
    """
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, 'Booking is confirmed')
            return redirect('mybookings_page')
        else:
            messages.error(
                request, 'Invalid, incorrect info or double booking')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)
