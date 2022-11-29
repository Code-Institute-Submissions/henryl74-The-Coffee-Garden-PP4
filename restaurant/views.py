from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Booking
from .forms import OnlineForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

# Create your views here.


class Home(generic.DetailView):
    """
    Renders the Index page in the browser
    """
    template_name = 'index.html'

# The get request returns the template set out above
# In this case it was the index.html template
    def get(self, request):
        return render(request, 'index.html')


class BookingView(FormView):
    """
    Renders the Booking form page in the browser
    Using the OnlineForm created in the forms.py file
    When the booking form is completed and submitted
    the user is redirect to a thank you for booking
    message page.
    """
    template_name = 'booking.html'
    form_class = OnlineForm
    success_url = '/booking_confirmation/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class BookingConfirmation(generic.DetailView):
    """
    Renders a Booking Confirmation page in the browser
    """
    template_name = 'booking_confirmation.html'

    def get(self, request):
        return render(request, 'booking_confirmation.html')


class Menu(generic.DetailView):
    """
    Renders the Menu page in the browser
    """
    def get(self, request):
        return render(request, 'menu.html')


class SignIn(generic.DetailView):
    """
    Renders the Login page in the browser
    """

    def login_view(self, request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            return render(request, 'login.html')


class ListBookingView(generic.DetailView):
    """
    This is the view that will bring up the
    list of bookings for a particular users
    so that they can be edited or deleted
    """

    template_name = 'update_booking.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)

            return render(request, 'update_booking.html', {
                'bookings': bookings
            }
            )
        else:
            return redirect('account_login')


@login_required
def edit_booking_view(request, booking_id):
    """
    When a user is on the My Bookings page
    which can only be accessed if you are
    logged in, they can click on the edit button.
    This will bring them to a new page, where the booking
    they wish to edit, located using the booking id,
    appears, prepopulated with the current information.
    Once the user clicks on the submit changes button
    they will be redirected to the home page and a
    confimation message will appear.
    """

    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.user == request.user:
            if request.method == 'POST':
                form = OnlineForm(data=request.POST, instance=booking)
                if form.is_valid():
                    form.save()
                    # Pops up a message to the user when a booking is edited
                    messages.success(request, 'Your booking has been updated')
                    return redirect('/')
        else:
            messages.error(request, 'You do not have the authority to access this page!')
            return redirect('/')

    form = OnlineForm(instance=booking)

    return render(request, 'manage_bookings.html', {
        'form': form
        })


@login_required
def delete_booking(request, booking_id):
    """
    When a user is on the My Bookings page
    which can only be accessed if you are
    logged in, they can click on the cancel booking
    button. This will cancel the booking using its
    booking id, redirect the user back to the home page and
    pop up a confimation message will appear.
    """
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.user == request.user:
            booking.delete()
            # Pops up a message to the user when a bookings is cancelled
            messages.success(request, 'Your booking has been cancelled')
            return redirect('/')
        else:
            messages.error(request, 'You do not have the authority to access this page!')
            return redirect('/')
