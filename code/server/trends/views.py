from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from trends import view_handlers
import json

from trends.db import article


# Get IDs of latest articles
#
# Required parameters:
# - "page": Integer - n'th page of latest articles
#
# Output: JSONResponse
# {'success': boolean, 'latest': list(Integer)}
#
@csrf_exempt
def latest_articles(request, page):
    if request.method == 'GET':
        return view_handlers.handle_latest_articles(page)
    else:
        return HttpResponseBadRequest("500 Bad Request")


# Get preview data of article
#
# Required parameters:
# - "id": Integer - ID of article to fetch
#
# Output: JSONResponse
# {'success': boolean, 'article': {
#                           'title': String, 'abstract': String
#                           'author': String, 'date': Date,
#                           'time_to_read': Integer, 'image': String/URL
#                           'tags': list(String)}
#
@csrf_exempt
def article_abstract(request, article_id):
    if request.method == 'GET':
        media_uri = request.build_absolute_uri('/media/')
        return view_handlers.handle_article_abstract(article_id, media_uri)
    else:
        return JsonResponse({'success': 'false'})


# Get preview data of article
#
# Required parameters:
# - "id": Integer - ID of article to fetch
#
# Output: JSONResponse
# {'success': boolean, 'article': {
#                           'title': String, 'content': String
#                           'author': String, 'date': Date,
#                           'time_to_read': Integer, 'image': String/URL
#                           'tags': list(String)}
#
@csrf_exempt
def article_data(request, article_id):
    if request.method == 'GET':
        media_uri = request.build_absolute_uri('/media/')
        return view_handlers.handle_article_data(article_id, media_uri)
    else:
        return JsonResponse({'success': 'false'})


# Get IDs of articles by title and tags
#
# Required parameters:
# - "query": String - Search string
# - "page": Integer - Page of results
# - "tags": list(String) - List of tags
#
# Output: JSONResponse
# {'success': boolean, 'results': list(Integer)}
#
@csrf_exempt
def search(request):
    if request.method == 'GET':
        return JsonResponse({'success': 'false'})
    else:
        params = json.loads(request.body)
        return view_handlers.handle_search(params.get('tags'),
                                           params.get("query"),
                                           params.get("page"))


# Gets entire page of abstract data
#
# Required parameters:
# - "page": Integer - Page of results
#
# Output: JSONResponse
# {'success': boolean, 'data': list(/abstract JSON responses)}
#
@csrf_exempt
def abstract_page(request, page):
    if request.method == 'POST':
        return JsonResponse({'success': 'false'})
    else:
        media_uri = request.build_absolute_uri('/media/')
        return view_handlers.handle_abstract_page(page, media_uri)


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        return view_handlers.handle_contact(params.get('name'),
                                            params.get('email'),
                                            params.get('subject'),
                                            params.get('content'))


@csrf_exempt
def tags(request):
    if request.method == 'GET':
        return view_handlers.handle_tags()
