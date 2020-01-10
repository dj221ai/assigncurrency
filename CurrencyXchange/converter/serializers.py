from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserBalance, CurrencyConversion

UserRegisterModel = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     style={'input_type': 'password'}
                                     )

    def create(self, validated_data):
        user = UserRegisterModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserRegisterModel
        fields = ('id', 'first_name', 'last_name', 'username', 'password')


class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBalance
        fields = '__all__'


class CurrencyConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyConversion
        fields = '__all__'
