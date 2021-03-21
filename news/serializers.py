from rest_framework import serializers

from news.models import Comments, Posts


class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = [
            'id',
            'title',
            'creation_date',
            'author',
            'link',
            'vote_count',
        ]


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = [
            'author',
            'creation_date',
            'comment_content',
            'comment_post'
        ]
