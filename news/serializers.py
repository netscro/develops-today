from rest_framework import serializers

from news.models import Posts, Comments


class PostsSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Posts
        fields = [
            'title',
            'creation_date',
            'author',
            'link',
            'vote_count',
        ]


class CommentsSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comments
        fields = [
            'author',
            'creation_date',
            'comment_content',
            'comment_post'
        ]
