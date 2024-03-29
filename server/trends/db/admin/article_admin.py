from trends.db.obj.articleModel import Article, Tag
from trends.db import article


def create_article(title, author, abstract, body, date, time_to_read, image):
    a = Article(title=title, author=author, abstract=abstract, body=body,
                      date=date, time_to_read=time_to_read, image=image)
    a.save()
    return a


def edit_article(article_id, title=None, author=None, abstract=None, body=None, date=None, time_to_read=None, image=None):
    a = article.get_article(article_id)
    if a is None:
        return None
    if title:
        a.title = title
    if author:
        a.author = author
    if abstract:
        a.abstract = abstract
    if body:
        a.body = body
    if date:
        a.date = date
    if time_to_read:
        a.time_to_read = time_to_read
    if image:
        a.image = image

    a.save()
    return a


def delete_article(article_id):
    article_obj = Article.objects.filter(id=article_id)
    if article_obj:
        article_obj.delete()
        return True
    else:
        return False


def set_article_tags(article_id, tags):
    existing_tags = Tag.objects.filter(article__pk=article_id.pk)
    if existing_tags:
        existing_tags.delete()
    if tags:
        for tag in tags:
            t = Tag(tag=tag, article=article_id)
            t.save()
