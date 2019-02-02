from __future__ import unicode_literals

from django.contrib.auth.models import User

from django import forms

from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from django.db.models.signals import post_save
from django.dispatch import receiver

from  django.shortcuts import get_object_or_404

from wagtail.contrib.routable_page.models import RoutablePageMixin, route

class SitePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        #('column', ColumnBlocks()),
        #('column', blocks.ColumnBlocks())

    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

RSVP_CHOICES = (
    ('YES', 'Yes, I am delighted to attend'),
    ('NO', 'No, I am sorry, we will have to celebrate another time'),
)

class Event(models.Model):
    eventTitle = models.CharField(max_length=255)
    def __str__(self):
        return self.eventTitle

class Rsvp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, blank=True, null=True)
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
        return '%s - %s - %s' % (self.user, self.event, self.status)


class EventPage(RoutablePageMixin, Page):
    invitedUsers = ParentalManyToManyField(User, blank=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    eventTitle = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    date = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    thankyou_page_title = models.CharField(max_length=255, help_text="Title text to use for the 'thank you' page")
    content_panels = Page.content_panels + [
        FieldPanel('event'),
        FieldPanel('eventTitle'),
        FieldPanel('description'),
        FieldPanel('date'),
        FieldPanel('location'),
        FieldPanel('thankyou_page_title'),
        FieldPanel('invitedUsers', widget=forms.CheckboxSelectMultiple)
    ]

@route(r'^(\d+)/$')
def form_view(self, request, form_id=None):
    from .forms import EventRSVPForm
    from .models import Rsvp
    instance = get_object_or_404(Rsvp, id=form_id)

        #rsvp = RSVP.objects.get(pk=pk)
        #instance = get_object_or_404(Rsvp, id=rsvp)
        #instance = Rsvp.objects.get(pk=rsvp_id)
        #instance = Rsvp.objects.get(pk=rsvp.id)


        #form = EventRSVPForm(request.POST or None)
    if request.method == 'POST':
        form = EventRSVPForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
                #event.user = request.user
            event.event = self.event
            event.save()
            return render(request, 'flavours/thankyou.html', {
                'page': self,
                'event': event,
            })
    else:
        form = EventRSVPForm()

    return render(request, 'event/event_page.html', {
        'page': self,
        'form': form,
    })

@receiver(post_save, sender=User)
def create_rsvp(sender, instance, created, **kwargs):
    if created:
        Rsvp.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_rsvp(sender, instance, **kwargs):
    instance.rsvp.save()
