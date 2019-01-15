from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)
from event.models import Rsvp, Event

class EventAdmin(ModelAdmin):
    model = Event
    filter_horizontal = ('user')

class RSVPAdmin(ModelAdmin):
    model = Rsvp
    list_display = ('user', 'event', 'event')
    #list_filter = ('event', 'status')

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(RSVPAdmin)
modeladmin_register(EventAdmin)
