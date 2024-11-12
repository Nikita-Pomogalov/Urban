from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
# Create your views here.


def index(request):
    page_size = int(request.GET.get('page_size', 5))
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, page_size)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj, 'page_size': page_size})
