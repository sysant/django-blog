from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from django.db.models import Q, F
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    # 首页
    post_list = Post.objects.all()  # 查询所有文章,queryset数据
    paginator = Paginator(post_list, 3)  # 每页显示5条数据
    page_number = request.GET.get('page')   # 即转换为 ?page='页码'
    page_obj = paginator.get_page(page_number)

    data = {
        'post_list': post_list,
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', data)


def categroy_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # 获取分类下的所有文章
    posts = category.post_set.all()
    paginator = Paginator(posts, 3)  # 每页显示5条数据
    page_number = request.GET.get('page')   # 即转换为 ?page='页码'
    page_obj = paginator.get_page(page_number)
    context = {"category": category,
               "post_list": posts,
               "page_obj": page_obj,
               }
    return render(request, 'blog/list.html', context)


def post_detail(request, post_id):
    # 文章详情
    posts = get_object_or_404(Post, id=post_id)
    # 用文章 id 实现上下篇
    prev_post = Post.objects.filter(id__lt=post_id).last()  # 上一篇的文章
    next_post = Post.objects.filter(id__gt=post_id).first()  # 下一篇的文章
    # 增加阅读量
    Post.objects.filter(id=post_id).update(pv=F('pv') + 1)  # 增加阅读量,有漏洞，仅做思路
    # 用发布日期来实现上下篇 有问题，待调试
    # date_prev_post = Post.objects.filter(add_date__lt=post.add_date).last()     # 上一篇的文章
    # date_next_post = Post.objects.filter(add_date__gt=post.add_date).first()    # 下一篇的文章
    context = {'post': posts,
               'prev_post': prev_post,
               'next_post': next_post,
               }
    return render(request, 'blog/detail.html', context)


def search(request):
    """ 搜索功能 """
    keyword = request.GET.get('keyword')
    if not keyword:
        post_list = Post.objects.all()
    else:
        post_list = Post.objects.filter(Q(title__icontains=keyword) |
                                        Q(desc__icontains=keyword) | Q(content__icontains=keyword))
    paginator = Paginator(post_list, 3)  # 每页显示5条数据
    page_number = request.GET.get('page')   # 即转换为 ?page='页码'
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': post_list,
        'page_obj': page_obj
    }
    return render(request, 'blog/index.html', context=context)


def archives(request, year, month):
    """ 文章归档功能 """
    post_list = Post.objects.filter(add_date__year=year, add_date__month=month)
    paginator = Paginator(post_list, 3)     # 每页显示5条数据
    page_number = request.GET.get('page')   # 即转换为 ?page='页码'
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': post_list,
        'year': year,
        'month': month,
        'page_obj': page_obj
    }
    return render(request, 'blog/sidebar/archives_list.html', context=context)
