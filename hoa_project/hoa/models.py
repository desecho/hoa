# -*- coding: utf8 -*-
from django.db import models


class Hoa(models.Model):
    name = models.CharField('название', unique=True, max_length=255)
    location = models.CharField('местонахождение', max_length=255)
    phone = models.CharField('телефон', max_length=255)
    contact = models.CharField('ответственный', max_length=255)

    class Meta:
        verbose_name = 'ТСЖ'
        verbose_name_plural = 'ТСЖ'

    def __unicode__(self):
        return self.name


class Agreement(models.Model):
    hoa = models.ForeignKey(Hoa, verbose_name='ТСЖ')
    number = models.CharField('номер', max_length=255)
    ammount = models.IntegerField('сумма')
    date = models.DateField('дата')
    comment = models.CharField('комментарий', max_length=255, null=True, blank=True)
    deleted = models.BooleanField('удален')

    class Meta:
        verbose_name = 'договор'
        verbose_name_plural = 'договора'

    def __unicode__(self):
        return self.number


class Address(models.Model):
    agreement = models.ForeignKey(Agreement, verbose_name='договор')
    street = models.CharField('улица', max_length=255)
    house = models.CharField('дом', max_length=255)

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'

    def __unicode__(self):
        return self.street + ' ' + self.house

class Payment(models.Model):
    agreement = models.ForeignKey(Agreement, verbose_name='договор')
    ammount = models.IntegerField('сумма')
    date = models.DateField('дата')
    period_start = models.DateField('дата начала периода')
    period_end = models.DateField('дата конца периода')
    comment = models.CharField('комментарий', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'

    def __unicode__(self):
        return '%s %d' % (self.agreement, self.ammount)
