from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from WebApp.models import PurchaseMemo, SaleMemo, Customer, Supplier, Item, ReturnSaleMemo


def purchase(request):
    objects= PurchaseMemo.objects.all()
    if request.POST.get('filterButton'):
        dateFilter = request.POST.get('dateFilter','')
        nameFilter = request.POST.get('nameFilter','')

        dateFrom = request.POST.get('dateFrom', '')
        dateTo = request.POST.get('dateTo', '')
        selectParty = request.POST.get('selectParty', '')
        if dateFilter=='on' and nameFilter== 'on':
            if dateFrom=='' or dateTo =='' or selectParty =='':
                objects =PurchaseMemo.objects.filter(id=-1)
            else:
                party= Supplier.objects.filter(id=int(selectParty))
                objects = PurchaseMemo.objects.filter(date__range=[dateFrom, dateTo],party=party)
        elif dateFilter =='on':
            if dateFrom=='' or dateTo =='':
                objects =PurchaseMemo.objects.filter(id=-1)
            else:
                objects = PurchaseMemo.objects.filter(date__range=[dateFrom, dateTo])
        elif nameFilter =='on':
            if selectParty =='':
                objects =PurchaseMemo.objects.filter(id=-1)
            else:
                party= Supplier.objects.filter(id=int(selectParty))
                objects = PurchaseMemo.objects.filter(party=party)



    c = {'OBJECTS': objects, 'NAME': Supplier.objects.all() }
    c.update(csrf(request))
    return render_to_response('rpt_purchase.html', c)


def sale(request):
    objects= SaleMemo.objects.all()
    dateFilter = request.POST.get('dateFilter', '')
    nameFilter = request.POST.get('nameFilter', '')

    dateFrom = request.POST.get('dateFrom', '')
    dateTo = request.POST.get('dateTo', '')
    selectParty = request.POST.get('selectParty', '')
    if dateFilter == 'on' and nameFilter == 'on':
        if dateFrom == '' or dateTo == '' or selectParty == '':
            objects = SaleMemo.objects.filter(id=-1)
        else:
            party = Customer.objects.filter(id=int(selectParty))
            objects = SaleMemo.objects.filter(date__range=[dateFrom, dateTo], party=party)
    elif dateFilter == 'on':
        if dateFrom == '' or dateTo == '':
            objects = SaleMemo.objects.filter(id=-1)
        else:
            objects = SaleMemo.objects.filter(date__range=[dateFrom, dateTo])
    elif nameFilter == 'on':
        if selectParty == '':
            objects = SaleMemo.objects.filter(id=-1)
        else:
            party = Customer.objects.filter(id=int(selectParty))
            objects = SaleMemo.objects.filter(party=party)

    c = {'OBJECTS': objects, 'NAME': Customer.objects.all()}
    c.update(csrf(request))
    return render_to_response('rpt_sale.html', c)


def salesReturn(request):
    objects= ReturnSaleMemo.objects.all()
    if request.POST.get('filterButton'):
        dateFilter = request.POST.get('dateFilter','')
        nameFilter = request.POST.get('nameFilter','')

        dateFrom = request.POST.get('dateFrom', '')
        dateTo = request.POST.get('dateTo', '')
        selectParty = request.POST.get('selectParty', '')
        if dateFilter=='on' and nameFilter== 'on':
            if dateFrom=='' or dateTo =='' or selectParty =='':
                objects =ReturnSaleMemo.objects.filter(id=-1)
            else:
                party= Customer.objects.filter(id=int(selectParty))
                objects = ReturnSaleMemo.objects.filter(date__range=[dateFrom, dateTo],party=party)
        elif dateFilter =='on':
            if dateFrom=='' or dateTo =='':
                objects =ReturnSaleMemo.objects.filter(id=-1)
            else:
                objects = ReturnSaleMemo.objects.filter(date__range=[dateFrom, dateTo])
        elif nameFilter =='on':
            if selectParty =='':
                objects =ReturnSaleMemo.objects.filter(id=-1)
            else:
                party= Customer.objects.filter(id=int(selectParty))
                objects = ReturnSaleMemo.objects.filter(party=party)


    c = {'OBJECTS': objects, 'NAME': Customer.objects.all()}
    c.update(csrf(request))
    return render_to_response('rpt_sale_return.html', c)


def listOfCustomers(request):
    objects = Customer.objects.all()
    c = {'OBJECTS': objects, }
    c.update(csrf(request))
    return render_to_response('report_list_of_customer.html', c)


def listOfSupplier(request):
    objects = Supplier.objects.all()
    c = {'OBJECTS': objects, }
    c.update(csrf(request))
    return render_to_response('report_list_of_supplier.html', c)


def listOfProduct(request):
    objects = Item.objects.all()
    c = {'OBJECTS': objects, }
    c.update(csrf(request))
    return render_to_response('report_list_of_product.html', c)