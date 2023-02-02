from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from youtube_process_video.models import YoutubeVideo
from youtube_process_video.serializers import YoutubeVideoSerializer


@api_view(('GET',))
def get_videos(request, page):
    video_list = YoutubeVideo.objects.all().order_by('-published_date')
    paginator = Paginator(video_list, 25)
    try:
        video_list = paginator.page(page)
    except EmptyPage:
        # return last page
        video_list = paginator.page(paginator.num_pages)
    return Response(data=YoutubeVideoSerializer(video_list, many=True).data, status=200)


@api_view(('GET',))
def search_video(request):
    filter = request.GET.get('filter', '')
    filter_regex = filter.replace(' ', '|')
    video_list = YoutubeVideo.objects.all().filter(
        Q(title__iregex=filter_regex) | Q(description__iregex=filter_regex))[:30]
    return Response(data=YoutubeVideoSerializer(video_list, many=True).data, status=200)
