from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect

from .models import Asset, AssetType, Location, Building
#from .forms import UpdateAssetForm
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet

from haystack.forms import SearchForm
from tri.form import Form, Field
from tri.form.views import create_object, edit_object

from django.template import RequestContext

def index(request):
    assetsAll = Asset.objects.all()
    context = {'assetsAll': assetsAll}
    return render(request, 'assets/index.html', context)

def detailed(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    building = Building.objects.all()
    return render(request, 'assets/detailed.html', {'asset': asset, 'building':building})

#def edit(request, asset_id):
#    asset = get_object_or_404(Asset, id=asset_id)
#    building = Building.objects.all()
#    form = UpdateAssetForm(request.POST or None, instance=asset)
#    print ("Passed Post Test")
#    if form.is_valid():
#        print ("Form is valid")
#        form.save()
#        return redirect('index')
#    return render(request, 'assets/edit.html', {'asset': asset, 'form': form, 'building':building})

class EditForm(Form):
    assetNumber = Field.text()
    assetSerial = Field.text()
    assetType = Field.choices(attr=None, choices=Asset.objects.values('assetTypes__type'))
    model_number = Field.text()
    #location = Field.multi_choice(attr=None, choices=Location.objects.values_list('floor'))
    floor = Field.multi_choice_queryset(attr=None, choices=Asset.objects.only('locationInfo__floor'))



def edit(request, asset_id):
    form = EditForm(request=request)
    asset = get_object_or_404(Asset, id=asset_id)
    if form.is_valid() and request.method == 'POST':
        form.apply(asset)
        asset.save()
        return HttpResponseRedirect('/')

    return render(request, 'assets/edit.html', {'asset': asset, 'form': form})

class CustomSearchView(SearchView):
    template_name = 'search/test.html'
    #queryset = SearchQuerySet().filter(assetNumber='VA012345')[0]
    queryset = SearchQuerySet().filter(assetNumber__exact='VA012345')
    print (queryset.query)
    form_class = SearchForm
