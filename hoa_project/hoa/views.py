# -*- coding: utf8 -*-
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to
from hoa.forms import SearchForm
from datetime import datetime
from hoa.models import Hoa, Agreement, Address, Payment
from django.db.models import Sum
from django.conf import settings
import chromelogger as console


def logout_view(request):
    logout(request)
    return redirect('/login/')


@render_to('index.html')
@login_required
def home(request):
    return {}


@render_to('search.html')
@login_required
def search(request):
    def filter_results(name, address, agreement):
        def process_result(list):
            output = [x[0] for x in list]
            return output
        if name:
            results = Hoa.objects.filter(name__icontains=name)
        else:
            results = Hoa.objects.all()
        if address:
            where = 'CONCAT(`street`, " ", `house`) LIKE "%%' + address + '%%"'
            agreements = Address.objects.all().extra(where=[where]).values_list('agreement')
            agreements = process_result(agreements)
            hoas = Agreement.objects.filter(pk__in=agreements).values_list('hoa')
            hoas = process_result(hoas)
            results = results.filter(pk__in=hoas)
        if agreement:
            hoas = Agreement.objects.filter(number__icontains=agreement).values_list('hoa')
            hoas = process_result(hoas)
            results = results.filter(pk__in=hoas)
        results = results.order_by('name')
        return results
    hoas = None
    form = SearchForm(request.POST or None)
    if form.is_valid():
        hoas = filter_results(form.cleaned_data['name'],
                              form.cleaned_data['address'],
                              form.cleaned_data['agreement']).values('pk', 'name', 'location', 'phone', 'contact')
        for hoa in hoas:
            agreements = Agreement.objects.filter(hoa_id=hoa['pk'])
            hoa['agreements'] = []
            for agreement in agreements:
                addresses = Address.objects.filter(agreement=agreement)
                for address in addresses:
                    hoa['agreements'].append({'type': agreement.type, 'number': agreement.number, 'address': address.get_full_address(), 'number_of_points': address.number_of_points})
    return {'form': form, 'hoas': hoas}


@render_to('debt.html')
@login_required
def debt(request):
    def count_months(date):
        return date.month + date.year * 12

    def biggest_date(date1, date2):
        if date1 > date2:
            return date1
        else:
            return date2

    def get_total_paid():
        total_paid = Payment.objects.filter(agreement=agreement).aggregate(Sum('ammount')).values()[0]
        if not total_paid:
            total_paid = 0
        return total_paid

    agreements = Agreement.objects.all()
    today = count_months(datetime.today())
    start_date = datetime.date(datetime.strptime(settings.START_DATE, settings.FORMAT_DATE))
    debts = []
    total = 0
    for agreement in agreements:
        date = biggest_date(agreement.date_start, start_date)
        if agreement.date_end is not None:
            pay_date = count_months(agreement.date_end)
        else:
            pay_date = today
        date = count_months(date)
        total_paid = get_total_paid()
        total_cost = (pay_date - date) * agreement.ammount
        debt = total_cost - total_paid
        if debt > 0:
            debts.append((agreement.hoa.name, agreement.number, debt))
            total += debt
    return {'debts': debts, 'total': total}


@render_to('info.html')
@login_required
def info(request):
    total_monthly = Agreement.objects.filter(date_end=None).aggregate(Sum('ammount')).values()[0]
    return {'total_monthly': total_monthly}
