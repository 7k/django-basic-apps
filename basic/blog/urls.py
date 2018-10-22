from django.conf.urls import *

from .views import *
from .feeds import *

urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        view=PostDetail.as_view(),
        name='blog_detail'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        view=PostArchiveDay.as_view(),
        name='blog_archive_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        view=PostArchiveMonth.as_view(),
        name='blog_archive_month'
    ),
    url(r'^(?P<year>\d{4})/$',
        view=PostArchiveYear.as_view(),
        name='blog_archive_year'
    ),
    url(r'^categories/(?P<slug>[-\w]+)/$',
        view=CategoryDetail.as_view(),
        name='blog_category_detail'
    ),
    url (r'^categories/$',
        view=CategoryList.as_view(),
        name='blog_category_list'
    ),
    url(r'^tags/(?P<slug>[-\w]+)/$',
        view=TagDetail.as_view(),
        name='blog_tag_detail'
    ),
    url (r'^search/$',
        view=search,
        name='blog_search'
    ),
    url(r'^$',
        view=PostList.as_view(),
        name='blog_index'
    ),
    url(r'^rss/$', BlogPostsFeed()),
    url(r'^categories/(?P<slug>[-\w]+)/rss/$', BlogPostsByCategory()),
]
