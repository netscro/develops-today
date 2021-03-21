from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from news.models import Comments, Posts
from news.serializers import CommentsSerializer, PostsSerializer


class PostsViewAPI(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class CommentsViewAPI(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class PostVotesUp(APIView):

    def post(self, request, pk):
        post = get_object_or_404(Posts, id=pk)
        post.vote_count += 1
        post.save()
        return Response(status=201)
