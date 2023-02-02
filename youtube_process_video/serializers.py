from youtube_process_video.models import YoutubeVideo
from rest_framework import serializers


class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = '__all__'
