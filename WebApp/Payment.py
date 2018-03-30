from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from WebApp.models import Supplier, Customer


def payment(request):

    party = Supplier.objects.all()
    customer = Customer.objects.all()
    c={'PARTY':party,'CUSTOMER':customer}
    c.update(csrf(request))
    return render_to_response('payment.html', c)