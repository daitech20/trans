from django.shortcuts import render, redirect
from .forms import InfoForm
from .transport import get_shipment
from django.http import HttpResponse
# Create your views here.

def Index(request):
    form = InfoForm()
    has_post = False
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            body = {
                'from_street_1': form.cleaned_data['from_street1'],
                'from_street_2': form.cleaned_data['from_street2'],
                'from_zip': form.cleaned_data['from_zip'],
                'from_country': form.cleaned_data['from_country'],
                'from_phone': form.cleaned_data['from_phone'],

                'to_street_1': form.cleaned_data['to_street1'],
                'to_street_2': form.cleaned_data['to_street2'],
                'to_zip': form.cleaned_data['to_zip'],
                'to_country': form.cleaned_data['to_country'],
                'to_phone': form.cleaned_data['to_phone'],

                'length': form.cleaned_data['length'],
                'width': form.cleaned_data['width'],
                'height': form.cleaned_data['height'],
                'weight': form.cleaned_data['weight']
            }
            print(body)
            shipment = get_shipment(body)
            has_post = True

            for rate in shipment.rates:
                print(rate.carrier)
                print(rate.service)
                print(rate.rate)
                print(rate.id)

            has_trans = len(shipment.rates)

            return render(request, "core/index.html", {'form': form,
                                                       'has_post': has_post,
                                                       'has_trans': has_trans,
                                                       'shipment': shipment})
        else:
            print("False")

    return render(request, "core/index.html", {'form': form})
