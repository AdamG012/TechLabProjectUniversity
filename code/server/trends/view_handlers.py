import datetime

from django.core.files import File
from django.http import JsonResponse

from server.settings import MEDIA_ROOT
from trends.db import article, contact
from trends.db.admin import article_admin
from trends.db.obj.articleModel import Article


def handle_latest_articles(pagenumber):
    latest = article.get_latest_page(int(pagenumber))
    if latest:
        return JsonResponse({'success': 'true', 'latest': latest}, safe=False)
    else:
        return JsonResponse({'success': 'false'})


def handle_article_abstract(article_id, uri):
    article_obj = article.get_article(int(article_id))
    if article_obj is None:
        return JsonResponse({'success': 'false'})
    tags = article.get_tags_by_article(int(article_id))

    return JsonResponse({'success': 'true',
                         'article': {
                             'title': str(article_obj.title),
                             'abstract': str(article_obj.abstract),
                             'author': str(article_obj.author),
                             'date': str(article_obj.date),
                             'time_to_read': str(article_obj.time_to_read),
                             'image': uri + str(article_obj.image),
                             'tags': tags
                         }}, safe=False)


def handle_article_data(article_id, uri):
    article_obj = article.get_article(int(article_id))
    if article_obj is None:
        return JsonResponse({'success': 'false'})
    tags = article.get_tags_by_article(int(article_id))
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
                             'image': uri + str(article_obj.image),
                             'tags': tags
                         }}, safe=False)


def handle_search(tags, query, pagenumber):
    if query is None:
        return JsonResponse({'success': 'false'})
    if pagenumber is None:
        pagenumber = 1
    if tags:
        tags = [x.lower() for x in tags]
    results = article.search_by_title(query, int(pagenumber), tags=tags)
    return JsonResponse({'success': 'true', 'results': results}, safe=False)


def handle_abstract_page(pagenumber, uri):
    data = []
    latest = article.get_latest_page(int(pagenumber))
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
                         'image': uri + str(article_obj.image),
                         'tags': tags
                     }})

    return JsonResponse({'success': 'true', 'data': data}, safe=False)


def handle_article_new(title, author, abstract, body, date, time_to_read, image, tags):
    format_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    # Call admin methods on Article database
    new_article = article_admin.create_article(
        title,
        author,
        abstract,
        "",
        format_date,
        int(time_to_read),
        "",
    )

    article_admin.set_article_tags(new_article, [x.lower() for x in tags])

    # Save image
    if image:
        with open(MEDIA_ROOT + str(new_article.pk) + ".jpg", 'wb+') as file:
            for chunk in image.chunks():
                file.write(chunk)
        image_file = "img/" + str(new_article.pk) + ".jpg"
    else:
        image_file = Article._meta.get_field('image').get_default()

    with open('./article_html/' + str(new_article.pk) + ".html", "w") as f:
        file = File(f)
        file.write(body)

    article_admin.edit_article(new_article.pk,
                               body='./article_html/' + str(new_article.pk) + ".html",
                               image=image_file)

    return JsonResponse({'success': 'true'})


def handle_article_edit(article_id, title, author, abstract, body, date, time_to_read, image, tags):
    format_date = datetime.date.strftime(date, "%Y-%m-%d")

    if image:
        with open(MEDIA_ROOT + article_id + ".jpg", 'wb+') as file:
            for chunk in image.chunks():
                file.write(chunk)
        image_file = "img/" + article_id + ".jpg"
    else:
        image_file = Article._meta.get_field('image').get_default()

    with open('./article_html/' + article_id + ".html", "w") as f:
        file = File(f)
        file.write(body)

    if article_admin.edit_article(
            int(article_id),
            title=title,
            author=author,
            abstract=abstract,
            body='./article_html/' + article_id + ".html",
            date=format_date,
            time_to_read=int(time_to_read),
            image=image_file
    ):
        article_admin.set_article_tags(article_id, [x.lower() for x in tags])
        return JsonResponse({'success': 'true'})

    return JsonResponse({'success': 'false'})


def handle_article_remove(article_id):
    if article_admin.delete_article(int(article_id)):
        return JsonResponse({'success': 'true'})
    return JsonResponse({'success': 'false'})


def handle_contact(name, email, subject, content):
    if contact.add_contact_request(name, email, subject, content):
        return JsonResponse({'success': 'true'})
    return JsonResponse({'success': 'false'})
