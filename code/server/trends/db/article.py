from trends.db.obj.articleModel import Article, Tag
from django.db.models import QuerySet


def get_article(article_id):
    return Article.objects.filter(id=article_id).first()


def get_articles_by_tag(tag):
    article_ids = Tag.objects.filter(tag=tag).values_list('article', flat=True)
    return list(Article.objects.filter(id__in=list(article_ids)).values_list('ids', flat=True))


def get_tags_by_article(article_id):
    return list(Tag.objects.filter(article=article_id).values_list('tag', flat=True))


def get_latest_page(page):
    if page <= 0:
        return None
    NUM_RESULTS = 8
    results = Article.objects.order_by('-date', '-id').values_list('id', flat=True)
    first_page = min((page - 1) * NUM_RESULTS, results.count())
    last_page = min(page * NUM_RESULTS, results.count())

    return list(results[first_page:last_page])


def search_by_title(query, page, tags=None):
    if page <= 0:
        return None

    NUM_RESULTS = 8

    if tags:
        results = Article.objects.none()
        for tag in tags:
            results.union(get_articles_by_tag(tag))
        results = results.filter(title__contains=query).order_by('-date', '-id')
    else:
        results = Article.objects.filter(title__contains=query).order_by('-date', '-id')

    first_page = min((page - 1) * NUM_RESULTS, results.count())
    last_page = min(page * NUM_RESULTS, results.count())
    return list(results[first_page:last_page].values_list('id', flat=True))