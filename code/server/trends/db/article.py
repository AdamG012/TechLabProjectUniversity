from trends.db.obj.articleModel import Article, Tag
from django.db.models import QuerySet


def get_article(article_id):
    return Article.objects.filter(id=article_id).first()


def get_articles_by_tag(tag):
    article_ids = Tag.objects.filter(tag=tag).values_list('article', flat=True)
    return Article.objects.filter(id__in=list(article_ids))


def get_tags_by_article(article_id):
    return list(Tag.objects.filter(article=article_id).values_list('tag', flat=True))


def get_abstract_page(page, tags=None):
    num_articles = 8
    articles = QuerySet()
    if tags:
        for tag in tags:
            articles.union(get_articles_by_tag(tag))
        articles = articles.order_by('-date', '-id')[page*num_articles:(page+1)*num_articles]
    else:
        articles = Article.objects.order_by('-date', '-id')[page*num_articles:(page+1)*num_articles]

    return articles.values('title', 'abstract', 'image', 'author')
