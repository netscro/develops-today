from celery import shared_task

from news.models import Posts


@shared_task
def test_task():
    return 5 + 5


@shared_task
def clear_votes():
    posts = Posts.objects.all()
    for post in posts:
        post.vote_count.clear()
