from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
        latest = article.get_latest_page(int(request.POST.get('PageNumber')))
        if latest:
            return JsonResponse({'success': 'true', 'latest': latest}, safe=False)
        else:
            return JsonResponse({'success': 'false'})


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
        article_obj = article.get_article(request.POST.get("id"))
        if article_obj is None:
            return JsonResponse({'success': 'false'})
        tags = article.get_tags_by_article(request.POST.get("id"))

        return JsonResponse({'success': 'true',
                             'article': {
                                 'title': str(article_obj.title),
                                 'abstract': str(article_obj.abstract),
                                 'author': str(article_obj.author),
                                 'date': str(article_obj.date),
                                 'time_to_read': str(article_obj.time_to_read),
                                 'image': str(article_obj.image),
                                 'tags': tags
                             }}, safe=False)


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
        article_obj = article.get_article(article_id)
        if article_obj is None:
            return JsonResponse({'success': 'false'})
        tags = article.get_tags_by_article(article_id)
        with open(str(article_obj.body), "r") as file:
            content = file.read()
            file.close()

        return JsonResponse({'success': 'true',
                             'article': {
                                 'title': str(article_obj.title),
                                 'content': content,
                                 'author': str(article_obj.author),
                                 'date': str(article_obj.date),
                                 'time_to_read': str(article_obj.time_to_read),
                                 'image': str(article_obj.image),
                                 'tags': tags
                             }}, safe=False)
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
        tags = request.POST.getlist('tags')
        results = article.search_by_title(request.POST.get("query"), request.POST.get("page"), tags=tags)
        return JsonResponse({'success': 'true', 'results': results}, safe=False)
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
        data = []
        latest = article.get_latest_page(int(request.POST.get('PageNumber')))
        for i in latest:
            article_obj = article.get_article(i)
            tags = article.get_tags_by_article(i)

            data.append({'success': 'true',
                         'article': {
                             'title': str(article_obj.title),
                             'abstract': str(article_obj.abstract),
                             'author': str(article_obj.author),
                             'date': str(article_obj.date),
                             'time_to_read': str(article_obj.time_to_read),
                             'image': str(article_obj.image),
                             'tags': tags
                         }})

        return JsonResponse({'success': 'true', 'data': data}, safe=False)
    else:
        return JsonResponse({'success': 'false'})

