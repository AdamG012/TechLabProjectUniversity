import datetime
import uuid

from django.http import HttpResponseBadRequest, JsonResponse
from django.core.files.storage import default_storage
from django.core.files import File
from trends.db.admin import article_admin


def article_new(request):
    if not request.user.is_authenticated:
        return HttpResponseBadRequest("Authentication error")

    if request.method == 'POST':
        new_article = article_admin.create_article(
            request.POST['title'],
            request.POST['author'],
            request.POST['abstract'],
            "",
            request.POST['date'],
            request.POST['time_to_read'],
            request.POST['image'],
        )

        with open('/article_html/' + new_article.pk + ".html", "w") as f:
            file = File(f)
            file.write(request.POST['body'])

        article_admin.edit_article(new_article.pk, body='/article_html/' + new_article.pk + ".html")
    else:
        return HttpResponseBadRequest("Bad Request")

def article_edit(request):
    if not request.user.is_authenticated:
        return HttpResponseBadRequest("Authentication error")

    if request.method == 'POST':
        id = int(request.POST['id'])
        date = datetime.date.strftime(request.POST['date'], "%Y-%m-%d")
        time_to_read = int(request.POST['time_to_read'])
        with open('/article_html/' + request.POST['id'] + ".html", "w") as f:
            file = File(f)
            file.write(request.POST['body'])

        article_admin.edit_article(
            id,
            request.POST['title'],
            request.POST['author'],
            request.POST['abstract'],
            '/article_html/' + request.POST['id'] + ".html",
            date,
            time_to_read,
            request.POST['image'],
        )
    else:
        return HttpResponseBadRequest("Bad Request")
