from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


from api.serializers import ChannelSerializer
from tvguide.models import Channel

@api_view(['GET'])
def channels(request):
    channels = Channel.objects.all()
    serializer = ChannelSerializer(channels, many=True)
    return Response(serializer.data)

#first testing
# def channels(request):
#     channels = Channel.objects.all()
#     serializer = ChannelSerializer(channels, many=True)
#     return JsonResponse(serializer.data, safe=False)
