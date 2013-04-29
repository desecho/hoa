# -*- coding: utf8 -*-
from django import forms

class SearchForm(forms.Form):
    name = forms.CharField(label='Название', required=False)
    address = forms.CharField(label='Адрес', required=False)
    agreement = forms.CharField(label='Номер договора', required=False)