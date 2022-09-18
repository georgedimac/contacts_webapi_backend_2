# from django.contrib.auth.models import User
from contacts_webapi.contacts_webapi.models import Contact
from rest_framework import viewsets
from contacts_webapi.contacts_webapi.serializers import ContactSerializer

#from rest_framework.views import APIView
#from rest_framework.response import Response

class ContactListViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows users to be viewed or edited.
    """
   
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    