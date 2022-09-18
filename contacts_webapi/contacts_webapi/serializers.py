# from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Contact

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        # fields = ["name", "email", "phone",]
        fields = "__all__"