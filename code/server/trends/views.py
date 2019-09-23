from django.http import HttpResponseBadRequest, JsonResponse
from trends.db import article


def latest_articles(request):
    if request.method == 'GET':
        return HttpResponseBadRequest("500 Bad Request")
    else:
        latest = article.get_latest_page(int(request.POST['PageNumber']))
        if latest:
            return JsonResponse({'success': 'true', 'latest': latest})
        else:
            return JsonResponse({'success': 'false'})


def article_abstract(request):
    if request.method == 'GET':
        return JsonResponse({'success': 'false'})
    else:
        article_obj = article.get_article(request.POST["id"])
        if article_obj is None:
            return JsonResponse({'success': 'false'})
        tags = article.get_tags_by_article(request.POST["id"])

        return JsonResponse({'success': 'true',
                             'article': {
                                 'title': str(article_obj.values('title')),
                                 'abstract': str(article_obj.values('abstract')),
                                 'author': str(article_obj.values('author')),
                                 'image': str(article_obj.values('image')),
                                 'tags': tags
                             }})


def article_data(request, article_id):
    if request.method == 'GET':
        article_obj = article.get_article(article_id)
        if article_obj is None:
            return JsonResponse({'success': 'false'})
        tags = article.get_tags_by_article(article_id)

        return JsonResponse({'success': 'true',
                             'article': {
                                 'title': str(article_obj.values('title')),
                                 'content': str(article_obj.values('body')),
                                 'image': str(article_obj.values('image')),
                                 'author': str(article_obj.values('author')),
                                 'tags': tags
                             }})
    else:
        return JsonResponse({'success': 'false'})


def search(request):
    if request.method == 'POST':
        results = article.search_by_title(request.POST['query'], request.POST['page'])
        return JsonResponse({'success': 'true', 'results': results})
    else:
        return JsonResponse({'success': 'false'})
