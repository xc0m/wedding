from django.db import models
from django.contrib.auth.models import User

RSVP_CHOICES = (
    ('YES', 'Yes, I am delighted to attend'),
    ('NO', 'No, I am sorry, we will have to celebrate another time'),
)

class Event(models.Model):
    eventTitle = models.CharField(max_length=255)
    def __str__(self):
        return '%s - %s' % (self.id, self.eventTitle)

class Rsvp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="RSVPUser")
    eventName = models.ForeignKey(Event,on_delete=models.CASCADE, blank=True)
    guestOne = models.CharField(max_length=255)
    guestTwo = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    address = models.TextField()
    status = models.CharField(
        null=True,
        default=None,
        max_length=3,
        choices=RSVP_CHOICES,
    )
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s - %s - %s - %s' % (self.id, self.user, self.eventName, self.status)
