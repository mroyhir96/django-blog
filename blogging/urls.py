from django.urls import path
from blogging.views import PostListView, PostDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
]

urlpatterns += staticfiles_urlpatterns()

""" urlpatterns += urlpatterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
 ) """
