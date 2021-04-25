import json

from django.test import TestCase
from trends.db.admin import article_admin as article
from trends import view_handlers
from trends.db.obj.articleModel import Article


class ArticleTest(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_article_methods(self):
        view_handlers.handle_article_new("Title", "Author", "Abstract", "Body", "2019-06-06", "123", "", [])

        j = json.loads(view_handlers.handle_search([], "", None).content)
        a_pk = j['results'][0]
        a = Article.objects.get(id=a_pk)

        response = view_handlers.handle_article_data(a_pk, "http://localhost:8000/")
        self.assertEqual('{"success": "true", '
                         '"article": {'
                             '"title": "Title", '
                             '"content": "Body", '
                             '"author": "Author", '
                             '"date": "2019-06-06", '
                             '"time_to_read": "123", '
                             '"image": "http://localhost:8000/img/Blank.jpg", '
                             '"tags": []'
                         '}}',
                         response.content.decode('utf-8'))

        view_handlers.handle_article_new("a", "b", "c", "d", "2019-06-01", "456", "", ["tag"])

        j = json.loads(view_handlers.handle_search([], "", None).content)
        b_pk = j['results'][1]
        b = Article.objects.get(id=b_pk)

        response = view_handlers.handle_article_data(b_pk, "http://localhost:8000/")
        self.assertEqual('{"success": "true", '
                         '"article": {'
                             '"title": "a", '
                             '"content": "d", '
                             '"author": "b", '
                             '"date": "2019-06-01", '
                             '"time_to_read": "456", '
                             '"image": "http://localhost:8000/img/Blank.jpg", '
                             '"tags": ["tag"]'
                         '}}',
                         response.content.decode('utf-8'))

        article.delete_article(a_pk)
        response = view_handlers.handle_article_data(a_pk, "http://localhost:8000/")
        self.assertEqual('{"success": "false"}',
                         response.content.decode('utf-8'))

        response = view_handlers.handle_article_data(b_pk, "http://localhost:8000/")
        self.assertEqual('{"success": "true", '
                         '"article": {'
                             '"title": "a", '
                             '"content": "d", '
                             '"author": "b", '
                             '"date": "2019-06-01", '
                             '"time_to_read": "456", '
                             '"image": "http://localhost:8000/img/Blank.jpg", '
                             '"tags": ["tag"]'
                         '}}',
                         response.content.decode('utf-8'))

        view_handlers.handle_article_edit(str(b_pk), "e", "f", "g", "h", "2019-06-05", "789", "", ["tag1", "tag2"])
        response = view_handlers.handle_article_data(b_pk, "http://localhost:8000/")
        self.assertEqual('{"success": "true", '
                         '"article": {'
                             '"title": "e", '
                             '"content": "h", '
                             '"author": "f", '
                             '"date": "2019-06-05", '
                             '"time_to_read": "789", '
                             '"image": "http://localhost:8000/img/Blank.jpg", '
                             '"tags": ["tag1", "tag2"]'
                         '}}',
                         response.content.decode('utf-8'))
