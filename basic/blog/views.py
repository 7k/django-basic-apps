import datetime
import re

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic import DayArchiveView, DateDetailView
from django.views.generic import YearArchiveView, MonthArchiveView
from django.db.models import Q
from django.conf import settings

from basic.blog.models import *
from basic.tools.constants import STOP_WORDS_RE
from tagging.models import Tag, TaggedItem


class PostList(ListView):
    model = Post
    paginate_by = getattr(settings,'BLOG_PAGESIZE', 20)


class PostArchiveYear(YearArchiveView):
    queryset = Post.objects.published()
    date_field = 'publish'
    make_object_list = True


class PostArchiveMonth(MonthArchiveView):
    queryset = Post.objects.published()
    date_field = 'publish'


class PostArchiveDay(DayArchiveView):
    queryset = Post.objects.published()
    date_field = 'publish'


class PostDetail(DateDetailView):
    """
    Displays post detail. If user is superuser, view will display 
    unpublished post detail for previewing purposes.
    """
    date_field = 'publish'

    def get_queryset(self):
        posts = None
        if self.request.user.is_superuser:
            posts = Post.objects.all()
        else:
            posts = Post.objects.published()
        return posts


class CategoryList(ListView):
    model = Category


class CategoryDetail(DetailView):
    model = Category


class TagDetail(DetailView):
    model = Tag


def search(request, template_name='blog/post_search.html'):
    """
    Search for blog posts.

    This template will allow you to setup a simple search form that will try to return results based on
    given search strings. The queries will be put through a stop words filter to remove words like
    'the', 'a', or 'have' to help imporve the result set.

    Template: ``blog/post_search.html``
    Context:
        object_list
            List of blog posts that match given search term(s).
        search_term
            Given search term.
    """
    context = {}
    if request.GET:
        stop_word_list = re.compile(STOP_WORDS_RE, re.IGNORECASE)
        search_term = '%s' % request.GET['q']
        cleaned_search_term = stop_word_list.sub('', search_term)
        cleaned_search_term = cleaned_search_term.strip()
        if len(cleaned_search_term) != 0:
            post_list = Post.objects.published().filter(Q(title__icontains=cleaned_search_term) | Q(body__icontains=cleaned_search_term) | Q(tags__icontains=cleaned_search_term) | Q(categories__title__icontains=cleaned_search_term))
            context = {'object_list': post_list, 'search_term':search_term}
        else:
            message = 'Search term was too vague. Please try again.'
            context = {'message':message}
    return render_to_response(template_name, context, context_instance=RequestContext(request))
