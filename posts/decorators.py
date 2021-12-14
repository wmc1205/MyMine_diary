
from django.http import HttpResponseForbidden

from posts.models import Post


def posts_ownership_required(func):
    def decorated(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        if not post.writer == request.user:
            return HttpResponseForbidden()
        else:
            return func(request, *args, **kwargs)

    return decorated