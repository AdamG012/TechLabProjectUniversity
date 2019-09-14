from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from trends.db import article


def index(request):
    return HttpResponse("index")
    # TODO: Implement index page


def articleSnapshots(request):
    if request.method == 'GET':
        return HttpResponseBadRequest("500 Bad Request")
    else:
        article.get_abstract_page(request.POST['PageNumber'])
    # TODO: Return values for articleSnapshots


def article(request, article_id):
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
                                 'tags': str(','.join(tags))
                             }})
    else:
        return JsonResponse({'success': 'false'})


def search(request):
    return HttpResponse("search")
    # TODO: Implement search function