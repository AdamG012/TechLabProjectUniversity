import datetime

from django.contrib import auth
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.core.files import File
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
        date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()

        # Call admin methods on Article database
        new_article = article_admin.create_article(
            request.POST['title'],
            request.POST['author'],
            request.POST['abstract'],
            "",
            date,
            request.POST['time_to_read'],
            request.POST['image'],
        )

        with open('/article_html/' + new_article.pk + ".html", "w") as f:
            file = File(f)
            file.write(request.POST['body'])

        article_admin.edit_article(new_article.pk, body='/article_html/' + new_article.pk + ".html")

        return JsonResponse({'success': 'true'})
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
        article_id = int(request.POST['id'])
        date = datetime.date.strftime(request.POST['date'], "%Y-%m-%d")
        time_to_read = int(request.POST['time_to_read'])
        with open('/article_html/' + request.POST['id'] + ".html", "w") as f:
            file = File(f)
            file.write(request.POST['body'])

        if article_admin.edit_article(
            article_id,
            title=request.POST['title'],
            author=request.POST['author'],
            abstract=request.POST['abstract'],
            body='/article_html/' + request.POST['id'] + ".html",
            date=date,
            time_to_read=time_to_read,
            image=request.POST['image']
        ):
            return JsonResponse({'success': 'true'})
        return JsonResponse({'success': 'false'})
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
        article_id = int(request.POST["id"])
        if article_admin.delete_article(article_id):
            return JsonResponse({'success': 'true'})
        return JsonResponse({'success': 'false'})
    else:
        return HttpResponseBadRequest("Bad Request")


# Log into admin account (Admin only)
#
# Required parameters:
# - "username": String
# - "password": String (plaintext)
#
# Output: Nothing (changes user session cookies)
#
def login(request):
    user = auth.authenticate(username=request.POST["username"],
                             password=request.POST["password"])
    if user is not None and user.is_active:
        auth.login(request, user)


# Log out of account (Admin only)
#
# Required parameters: None
#
# Output: Nothing (changes user session cookies)
#
def logout(request):
    auth.logout(request)
