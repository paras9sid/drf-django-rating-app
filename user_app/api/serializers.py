from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username','email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True} 
        }

    # check password 1 and 2 same  and email is unique or not
    def save(self):

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        # check password 1 and 2 same - Validation
        if password != password2:
            raise serializers.ValidationError({'error': 'P1 and P2 aren\'t same !'})

        # check email is unique or not !
        queryset = User.objects.filter(email=self.validated_data['email'])
        if queryset.exists():
            raise serializers.ValidationError({'error': 'Email id is already used...'})

        # user creation manually
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
