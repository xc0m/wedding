from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import RSVPForm
from .models import Rsvp


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, event_str):
    #instance = Rsvp.objects.get(id=event_id)
    #instance =  Rsvp.objects.filter(id=event_id, user=request.user)
    print (event_str)
    queryset = Rsvp.objects.filter(eventName=event_str)
    instance = get_object_or_404(queryset, user=request.user)
    #instance = Rsvp.objects.select_related(request.user).get(id=event_id)
    #instance = get_object_or_404(Rsvp, id=event_id)
    form = RSVPForm(request.POST or None, instance=instance)
    print (request.user)
    print (instance.user)
    #if instance.user != request.user:
        #return HttpResponse("You are not allowed to edit this Post")
    if form.is_valid():
          form.save()
          return render(request, 'flavours/thankyou.html', {
              #'page': self,
              #'event': event,
          })
    return render(request, 'event/event_page.html', {'form': form})

def detail1(request, event_str):
        instance = get_object_or_404(Rsvp, id=event_id)
        #instance = Rsvp.objects.get(pk=event_id)
        form = RSVPForm(request.POST, instance=instance)
        #form = EventRSVPForm(request.POST or None)


        if request.method == 'POST':
            form = RSVPForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.user = request.user
                event.event = self.event
                event.save()
                return render(request, 'flavours/thankyou.html', {
                    #'page': self,
                    'event': event,
                })
        else:
            form = RSVPForm()

        return render(request, 'event/event_page.html', {
            #'page': self,
            'form': form,
        })
