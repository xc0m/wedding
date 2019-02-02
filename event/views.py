from django.shortcuts import render

def submit_rsvp(request, instance):
    from .forms import EventRSVPForm
    from .models import Rsvp
    #instance = Rsvp.objects.get(pk=rsvp.id)

    form = EventRSVPForm(request.POST or None, instance=self.instance.id)
    if request.method == 'POST':
        form = EventRSVPForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            #event.event = self.event
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
