from django.conf.urls.static import static
from django.urls import path

from server import settings
from trends import views, admin_views

urlpatterns = [
    path('search', views.search, name='search'),
    path('articles/<int:article_id>', views.article_data, name='article'),
    path('latest-articles/<int:page>', views.latest_articles, name='latest-articles'),
    path('abstract-page/<int:page>', views.abstract_page, name='abstract-page'),
    path('abstract/<int:article_id>', views.article_abstract, name='abstract'),
    path('contact', views.contact, name='contact'),
    path('tags', views.tags, name='tags'),
    path('admin/article-new', admin_views.article_new, name='article-new'),
    path('admin/article-edit', admin_views.article_edit, name='article-edit'),
    path('admin/article-remove', admin_views.article_remove, name='article-remove'),
    path('admin/login', admin_views.login, name='login'),
    path('admin/logout', admin_views.logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
