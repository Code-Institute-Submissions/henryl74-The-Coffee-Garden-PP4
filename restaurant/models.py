from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Options for how many custumers can book
CUSTOMERS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

# Time slots for the booking
TIME = (
    ('08:30', '08:30'),
    ('09:00', '09:00'),
    ('09:30', '09:30'),
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
)


class Booking(models.Model):
    """Model that is used to store the data that the user enters in the
    booking form. The User Foreignkey associates each booking
    with a particular user.
    """
    class Meta:
        unique_together = ('date', 'time', 'customers')

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_booking")
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20, null=False, blank=False, default='')
    customers = models.CharField(max_length=2, choices=CUSTOMERS, default='2')
    time = models.CharField(max_length=30, choices=TIME, default='09:00')
    date = models.DateField()

    def __str__(self):
        return self.name
