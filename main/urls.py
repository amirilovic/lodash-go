from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed
from main.models import Post


class BlogFeed(Feed):
    title = "MySite"
    description = "Some feeds about cloud technologies"
    link = "/blog/feed"

    def items(self):
        return Post.objects.all().order_by("-created")[:4]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return u"/blog/%d" % item.id


urlpatterns = patterns('',
  url(r'^feed$', BlogFeed()),
  url(r'^(?P<pk>\d+)$', DetailView.as_view(
    model=Post,
    template_name="post.html")),
  url(r'^tag/(?P<tag>\w+)$', 'main.views.tagpage'),
  url(r'^archives$', ListView.as_view(
    queryset=Post.objects.all().order_by("-created"),
    template_name="archive.html")),
  url(r'^', ListView.as_view(
    queryset=Post.objects.all().order_by("-created")[:2],
    template_name="blog.html")),
  )
