from django.urls import path
from blog.views import *
from .feeds import LatestPostsRSSFeed


app_name = "blog"


urlpatterns = [
    path("", blog_index, name="index"),
    path("<int:pid>", blog_single, name="single"),
    path("category/<str:cat_name>", blog_index, name="category"),
    path("tag/<str:tag_name>", blog_index, name="tag"),
    path("author/<str:author_username>", blog_index, name="author"),
    path("search/", blog_search, name="search"),
    path("rss/feed", LatestPostsRSSFeed())
]
