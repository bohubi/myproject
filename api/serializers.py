from rest_framework.serializers import ModelSerializer


# this is like forms but for api's

from tvguide.models import Channel

class ChannelSerializer(ModelSerializer):
    class Meta:
        # from the model channel, that has a name field and id
        model = Channel
        fields = ['id','name']