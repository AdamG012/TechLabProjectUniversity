import datetime

from django.contrib import auth
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt

from trends import view_handlers
from trends.db.admin import article_admin


# POST request handler for article creation (Admin only)
#
# Required parameters:
# - "title": String - Article title
# - "author": String - Article author name
# - "abstract": String - Short article summary/excerpt
# - "body": String - WYSIWYG HTML article data
# - "date": String - Article date, format "YYYY-MM-DD"
# - "time_to_read": Integer - Estimated time to read article, in minutes
# - "image": String/URL - URL to article image
#
# Output: JSONResponse
# {'success': boolean}, true if successful, false if otherwise
#
def article_new(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Permission denied")

    if request.method == 'POST':
        return view_handlers.handle_article_new(request.POST.get('title'),
                                                request.POST.get('author'),
                                                request.POST.get('abstract'),
                                                request.POST.get('body'),
                                                request.POST.get('date'),
                                                request.POST.get('time_to_read'),
                                                request.FILES.get('image'))
    else:
        return HttpResponseBadRequest("Bad Request")


# Request handler for article editing (Admin only)
#
# Required parameters:
# - "id": Integer - ID of article to be edited
# - "title": String - New article title
# - "author": String - New article author name
# - "abstract": String - New article abstract
# - "body": String - NewWYSIWYG HTML article data
# - "date": String - New article date, format "YYYY-MM-DD"
# - "time_to_read": Integer - New estimated time to read article, in minutes
# - "image": String/URL - New URL to article image
#
# Output: JSONResponse
# {'success': boolean}, true if successful, false if otherwise
#
def article_edit(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Permission denied")

    if request.method == 'POST':
        return view_handlers.handle_article_edit(request.POST.get('id'),
                                                 request.POST.get('title'),
                                                 request.POST.get('author'),
                                                 request.POST.get('abstract'),
                                                 request.POST.get('body'),
                                                 request.POST.get('date'),
                                                 request.POST.get('time_to_read'),
                                                 request.FILES.get('image'))
    else:
        return HttpResponseBadRequest("Bad Request")


# Request handler for article removal (Admin only)
#
# Required parameters:
# - "id": Integer - ID of article to be deleted
#
# Output: JSONResponse
# {'success': boolean}, true if successful, false if otherwise
#
def article_remove(request):
    if not request.user.is_authenticated:
        return HttpResponseBadRequest("Authentication error")

    if request.method == 'POST':
        return view_handlers.handle_article_remove(request.POST.get('id'))
    else:
        return HttpResponseBadRequest("Bad Request")


# Log into admin account (Admin only)
#
# Required parameters:
# - "username": String
# - "password": String (plaintext)
#
# Output: JSONResponse
# {'success': boolean}
#
@csrf_exempt
def login(request):
    user = auth.authenticate(username=request.POST["username"],
                             password=request.POST["password"])
    if user is not None and user.is_active:
        auth.login(request, user)
        return JsonResponse({'success': 'true'})
    else:
        return JsonResponse({'success': 'false'})


# Log out of account (Admin only)
#
# Required parameters: None
#
# Output: None
#
@csrf_exempt
def logout(request):
    auth.logout(request)
