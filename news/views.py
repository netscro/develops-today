from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from news.models import Posts, Comments
from news.serializers import PostsSerializer, CommentsSerializer


class PostsViewAPI(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class CommentsViewAPI(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
