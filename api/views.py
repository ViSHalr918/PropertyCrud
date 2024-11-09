from django.shortcuts import render

# Create your views here.

from api.serializers import PropertySerializer


from rest_framework.viewsets import ModelViewSet

from api.models import Property

class PropertyViewsetView(ModelViewSet):

    serializer_class=PropertySerializer


    queryset=Property.objects.all()





