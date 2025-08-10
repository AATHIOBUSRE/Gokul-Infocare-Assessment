from rest_framework import serializers
from .models import CrudModels

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudModels
        fields = '__all__'

    def validate(self, data):
        first_name = data.get('FirstName', '').lower()
        email = data.get('EmailId', '').lower()
        if first_name == 'rahul' and email.endswith('gmail.com'):
            raise serializers.ValidationError("Email ending with 'gmail.com' is not allowed for first name Rahul.")
        return data
