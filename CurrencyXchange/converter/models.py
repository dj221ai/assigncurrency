from django.contrib.auth.models import User
from django.db import models
import requests
import json


class UserBalance(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return str(self.name)


def converter():
    headers = {
        'content-type': 'application/json',
    }
    url = "https://openexchangerates.org/api/currencies.json"
    response = requests.get(url, headers=headers)
    result = json.loads(response.content.decode('utf-8'))

    currency_abbreviations = [(k, v) for k, v in result.items()]
    return tuple(currency_abbreviations)


CURRENCY_SYMBOLS = converter()


class CurrencyConversion(models.Model):
    Amount_to_convert = models.FloatField()
    convert_from = models.CharField(max_length=100, choices=CURRENCY_SYMBOLS, default='')
    convert_to = models.CharField(max_length=100, choices=CURRENCY_SYMBOLS, default='')



