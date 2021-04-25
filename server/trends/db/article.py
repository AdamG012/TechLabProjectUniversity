from trends.db.obj.articleModel import Article, Tag
from django.db.models import Count


def get_article(article_id):
    return Article.objects.filter(id=article_id).first()


def get_articles_by_tag(tag):
    article_ids = Tag.objects.filter(tag=tag).values_list('article', flat=True)
    return Article.objects.filter(id__in=list(article_ids)).values_list('id', 'date')


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


def search_article(query, page, tags=None):
    if page <= 0:
        return None

    NUM_RESULTS = 8

    # print(tags)
    if tags:
        results = None
        for tag in tags:
            if results is None:
                results = get_articles_by_tag(tag)
            else:
                results = results | get_articles_by_tag(tag)

        results = results.filter(title__icontains=query).order_by('-date', '-id') | results.filter(author__icontains=query).order_by('-date', '-id')
    else:
        results = Article.objects.filter(title__icontains=query).order_by('-date', '-id') | Article.objects.filter(author__icontains=query).order_by('-date', '-id')

    first_page = min((page - 1) * NUM_RESULTS, results.count())
    last_page = min(page * NUM_RESULTS, results.count())
    return list(results[first_page:last_page].values_list('id', flat=True))


def get_tags():
    results = Tag.objects.values("tag").annotate(num_tags=Count("id")).order_by("-num_tags", "tag").values_list("tag", flat=True)
    return list(results)
