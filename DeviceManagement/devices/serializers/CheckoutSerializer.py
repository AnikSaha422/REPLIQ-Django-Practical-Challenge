from rest_framework import serializers
from devices.models import Checkout

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = '__all__'
