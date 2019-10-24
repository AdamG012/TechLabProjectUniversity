from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from trends import view_handlers

from trends.db import article


# Get IDs of latest articles
#
# Required parameters:
# - "PageNumber": Integer - n'th page of latest articles
#
# Output: JSONResponse
# {'success': boolean, 'latest': list(Integer)}
#
@csrf_exempt
def latest_articles(request):
    if request.method == 'GET':
        return HttpResponseBadRequest("500 Bad Request")
    else:
        return view_handlers.handle_latest_articles(request.POST.get('PageNumber'))


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
def article_abstract(request):
    if request.method == 'GET':
        return JsonResponse({'success': 'false'})
    else:
        media_uri = request.build_absolute_uri('/media/')
        return view_handlers.handle_article_abstract(request.POST.get("id"), media_uri)


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
    if request.method == 'POST':
        return view_handlers.handle_search(request.POST.getlist('tags'),
                                           request.POST.get("query"),
                                           request.POST.get("page"))
    else:
        return JsonResponse({'success': 'false'})


# Gets entire page of abstract data
#
# Required parameters:
# - "pagenumber": Integer - Page of results
#
# Output: JSONResponse
# {'success': boolean, 'data': list(/abstract JSON responses)}
#
@csrf_exempt
def abstract_page(request):
    if request.method == 'POST':
        media_uri = request.build_absolute_uri('/media/')
        return view_handlers.handle_abstract_page(request.POST.get('PageNumber'), media_uri)
    else:
        return JsonResponse({'success': 'false'})


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        return view_handlers.handle_contact(request.POST.get('name'),
                                            request.POST.get('email'),
                                            request.POST.get('subject'),
                                            request.POST.get('content'))
