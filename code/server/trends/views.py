from django.http import HttpResponseBadRequest, JsonResponse
from trends.db import article


# Get IDs of latest articles
#
# Required parameters:
# - "PageNumber": Integer - n'th page of latest articles
#
# Output: JSONResponse
# {'success': boolean, 'latest': list(Integer)}
#
def latest_articles(request):
    if request.method == 'GET':
        return HttpResponseBadRequest("500 Bad Request")
    else:
        latest = article.get_latest_page(int(request.POST['PageNumber']))
        if latest:
            return JsonResponse({'success': 'true', 'latest': latest})
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
                                 'date': str(article_obj.values('date')),
                                 'time_to_read': str(article_obj.values('time_to_read')),
                                 'image': str(article_obj.values('image')),
                                 'tags': tags
                             }})


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
def article_data(request, article_id):
    if request.method == 'GET':
        article_obj = article.get_article(article_id)
        if article_obj is None:
            return JsonResponse({'success': 'false'})
        tags = article.get_tags_by_article(article_id)
        with open(str(article_obj.values('body')), "r") as file:
            content = file.read()
            file.close()

        return JsonResponse({'success': 'true',
                             'article': {
                                 'title': str(article_obj.values('title')),
                                 'content': content,
                                 'author': str(article_obj.values('author')),
                                 'date': str(article_obj.values('date')),
                                 'time_to_read': str(article_obj.values('time_to_read')),
                                 'image': str(article_obj.values('image')),
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
def search(request):
    if request.method == 'POST':
        tags = request.POST.getlist('tags')
        results = article.search_by_title(request.POST['query'], request.POST['page'], tags=tags)
        return JsonResponse({'success': 'true', 'results': results})
    else:
        return JsonResponse({'success': 'false'})
