# 自定义模板标签
# https://docs.djangoproject.com/zh-hans/3.2/howto/custom-template-tags/  官方自定义标签与过滤器文档

from django import template
from blog.models import Category, Sidebar, Post

register = template.Library()


@register.simple_tag
def get_category_list():
    # 全站分类
    return Category.objects.all()


@register.simple_tag
def get_sidebar_list():
    # 侧边栏
    return Sidebar.get_sidebar()


@register.simple_tag
def get_new_post():
    # 最新文章
    return Post.objects.order_by('-pub_date')[:8]


@register.simple_tag
def get_hot_post():
    # 热门文章
    return Post.objects.filter(is_hot=True)[:8]


@register.simple_tag
def get_hot2_post():
    # 热门文章 第二种实现
    return Post.objects.order_by('-pv')[:8]


@register.simple_tag
def get_archives():
    # 文章归档 https://docs.djangoproject.com/zh-hans/3.2/ref/models/querysets/#dates
    return Post.objects.dates('add_date', 'month', order='DESC')[:8]
