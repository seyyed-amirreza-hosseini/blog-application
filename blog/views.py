from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer get the first page
        posts = paginator.page(1)    
    except EmptyPage:
        # If page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)

    print(request.GET)  
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, post, year, month, day):
    post = get_object_or_404(
        Post, status=Post.Status.PUBLISHED, slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    
    return render(request, 'blog/post/detail.html', {'post': post})
