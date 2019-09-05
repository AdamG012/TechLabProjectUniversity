from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from db.trends_db import TrendsDB
# Create your views here.


def index(request):
    # TODO: Implement index page
    return HttpResponse("index")


def articleSnapshots(request):
    # TODO: Implement snapshots
    if request.method == 'GET':
        return HttpResponseBadRequest("404")


def article(request, article_id):
    if request.method == 'POST':
        return HttpResponseBadRequest("404")
    db = TrendsDB()
    response_data = {'success': False, 'article': None}

    try:
        article = db.get_article(article_id)
    except (TypeError, FileNotFoundError) as e:
        return response_data

    response_data['success'] = True
    # TODO: implement image and tags
    article_data = {'title': article.title, 'content': article.body,
                    'image': None, 'author': article.author, 'tags': []}

    return JsonResponse(article_data)


def search(request):
    if request.method == 'GET':
        return HttpResponseBadRequest("404")

    query = request.POST["searchQuery"]

    # TODO: Implement search feature
    return HttpResponse(query)