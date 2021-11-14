


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        