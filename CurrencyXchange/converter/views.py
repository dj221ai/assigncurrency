from django.shortcuts import render
from .models import UserBalance, CurrencyConversion
from .serializers import UserBalanceSerializer, UserCreationSerializer, CurrencyConversionSerializer
from rest_framework import viewsets, permissions, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import generics
import json
from pprint import pprint
import requests

headers = {
    'cache-control': "no-cache",
    'content-type': "application/json",
    'Accept': 'application/json'
}


class CreateUserView(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserCreationSerializer
    permission_classes = (permissions.AllowAny, )


class UserBalanceView(viewsets.ModelViewSet):
    queryset = UserBalance.objects.all()
    serializer_class = UserBalanceSerializer


class ConverterView(viewsets.ModelViewSet):
    queryset = CurrencyConversion.objects.all()
    serializer_class = CurrencyConversionSerializer

    def create(self, request, *args, **kwargs):
        try:
            url = "https://api.exchangeratesapi.io/latest"
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            param = {'converted_from': serializer.data['convert_from']}
            amount_given = serializer.data['Amount_to_convert']
            exchange_response = requests.get(url, headers=headers, params=param)
            exchange_result = json.loads(exchange_response.content.decode('utf-8'))
            rates = {
                'converted_from': serializer.data['convert_from'],
                'converted_to': serializer.data['convert_to'],
                'conversion_rate': exchange_result['rates'][serializer.data['convert_to']],
                'Amount': amount_given * exchange_result['rates'][serializer.data['convert_to']]
            }
            return Response(data=rates, status=status.HTTP_201_CREATED, headers=headers)

        except Exception as e:
            print(e)
            return Response(data='Sorry this currency rates not supported for now')

    def perform_create(self, serializer):
        serializer.save()

