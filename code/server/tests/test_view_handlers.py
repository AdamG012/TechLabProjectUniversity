import datetime
import json

from django.test import TestCase
from trends.db.obj.articleModel import Article, Tag
from trends import view_handlers


class ArticleTest(TestCase):
    def setUp(self):
        view_handlers.handle_article_new("Title",
                                         "Author",
                                         "Abstract",
                                         "Body",
                                         "2019-06-06",
                                         "123",
                                         "",
                                         ["Tag1", "Tag2"])
        view_handlers.handle_article_new("Another Title",
                                         "Another Author",
                                         "Another Abstract",
                                         "Another Body",
                                         "2019-06-07",
                                         "456",
                                         "",
                                         ["Tag1", "Tag3"])
        j = json.loads(view_handlers.handle_search([], "", None).content)
        self.ids = j['results']
        self.maxDiff = None

    def test_handle_latest_articles_false(self):
        response = view_handlers.handle_latest_articles(str(self.ids[0] + 1))
        self.assertEqual(b'{"success": "false"}', response.content)
        response = view_handlers.handle_latest_articles("-1")
        self.assertEqual(b'{"success": "false"}', response.content)

    def test_handle_article_abstract_false(self):
        response = view_handlers.handle_article_abstract(str(self.ids[0] + 1), "http://localhost:8000/")
        self.assertEqual(b'{"success": "false"}', response.content)
        response = view_handlers.handle_article_abstract("-1", "http://localhost:8000/")
        self.assertEqual(b'{"success": "false"}', response.content)

    def test_handle_article_data_false(self):
        response = view_handlers.handle_article_data(str(self.ids[0] + 1), "http://localhost:8000/")
        self.assertEqual(b'{"success": "false"}', response.content)
        response = view_handlers.handle_article_data("-1", "http://localhost:8000/")
        self.assertEqual(b'{"success": "false"}', response.content)

    def test_handle_article_edit_false(self):
        response = view_handlers.handle_article_edit(str(self.ids[0] + 1),
                                                     "Test Article",
                                                     "John",
                                                     "Testing testing",
                                                     "Testing article",
                                                     "2019-09-11",
                                                     "400000",
                                                     "",
                                                     [])
        self.assertEqual(b'{"success": "false"}', response.content)
        response = view_handlers.handle_article_edit("-1",
                                                     "Test Article",
                                                     "John",
                                                     "Testing testing",
                                                     "Testing article",
                                                     "2019-09-11",
                                                     "400000",
                                                     "",
                                                     [])
        self.assertEqual(b'{"success": "false"}', response.content)

    def test_handle_article_remove_false(self):
        response = view_handlers.handle_article_remove(str(self.ids[0] + 1))
        self.assertEqual(b'{"success": "false"}', response.content)
        response = view_handlers.handle_article_remove("-1")
        self.assertEqual(b'{"success": "false"}', response.content)

    def test_handle_abstract_page_false(self):
        response = view_handlers.handle_abstract_page("2", "http://localhost:8000/")
        response = view_handlers.handle_abstract_page("-1", "http://localhost:8000/")

    def test_handle_latest_articles(self):
        response = view_handlers.handle_latest_articles("1")
        self.assertEqual('{"success": "true", "latest": [' + str(self.ids[0]) + ', ' + str(self.ids[1]) + ']}',
                         response.content.decode('utf-8'))

    def test_handle_article_abstract(self):
        response = view_handlers.handle_article_abstract(self.ids[1], "http://localhost:8000/")
        self.assertEqual('{"success": "true", '
                         '"article": {'
                             '"title": "Title", '
                             '"abstract": "Abstract", '
                             '"author": "Author", '
                             '"date": "2019-06-06", '
                             '"time_to_read": "123", '
                             '"image": "http://localhost:8000/img/Blank.jpg", '
                             '"tags": ["tag1", "tag2"]'
                         '}}',
                         response.content.decode('utf-8'))

        response = view_handlers.handle_article_abstract(self.ids[0], "http://localhost:8000/")
        self.assertEqual('{"success": "true", '
                         '"article": {'
                             '"title": "Another Title", '
                             '"abstract": "Another Abstract", '
                             '"author": "Another Author", '
                             '"date": "2019-06-07", '
                             '"time_to_read": "456", '
                             '"image": "http://localhost:8000/img/Blank.jpg", '
                             '"tags": ["tag1", "tag3"]'
                         '}}',
                         response.content.decode('utf-8'))

    def test_handle_article_data(self):
        response = view_handlers.handle_article_data(self.ids[1], "http://localhost:8000/")
        self.assertEqual('{"success": "true", '
                         '"article": {'
                             '"title": "Title", '
                             '"content": "Body", '
                             '"author": "Author", '
                             '"date": "2019-06-06", '
                             '"time_to_read": "123", '
                             '"image": "http://localhost:8000/img/Blank.jpg", '
                             '"tags": ["tag1", "tag2"]'
                         '}}',
                         response.content.decode('utf-8'))

        response = view_handlers.handle_article_data(self.ids[0], "http://localhost:8000/")
        self.assertEqual('{"success": "true", '
                         '"article": {'
                             '"title": "Another Title", '
                             '"content": "Another Body", '
                             '"author": "Another Author", '
                             '"date": "2019-06-07", '
                             '"time_to_read": "456", '
                             '"image": "http://localhost:8000/img/Blank.jpg", '
                             '"tags": ["tag1", "tag3"]'
                         '}}',
                         response.content.decode('utf-8'))

    def test_handle_search(self):
        response = view_handlers.handle_search([], "Title", None)
        self.assertEqual('{"success": "true", '
                         '"results": [' + str(self.ids[0]) + ", " + str(self.ids[1]) + ']}',
                         response.content.decode('utf-8'))

        response = view_handlers.handle_search([], "Another", None)
        self.assertEqual('{"success": "true", '
                         '"results": [' + str(self.ids[0]) + ']}',
                         response.content.decode('utf-8'))

        response = view_handlers.handle_search(["tag1"], "", None)
        self.assertEqual('{"success": "true", '
                         '"results": [' + str(self.ids[0]) + ", " + str(self.ids[1]) + ']}',
                         response.content.decode('utf-8'))

        response = view_handlers.handle_search(["tag2", "tag3"], "", None)
        self.assertEqual('{"success": "true", '
                         '"results": [' + str(self.ids[0]) + ", " + str(self.ids[1]) + ']}',
                         response.content.decode('utf-8'))

        response = view_handlers.handle_search(["tag3", "tag2"], "", None)
        self.assertEqual('{"success": "true", '
                         '"results": [' + str(self.ids[0]) + ", " + str(self.ids[1]) + ']}',
                         response.content.decode('utf-8'))

        response = view_handlers.handle_search(["tag3"], "", None)
        self.assertEqual('{"success": "true", '
                         '"results": [' + str(self.ids[0]) + ']}',
                         response.content.decode('utf-8'))

        response = view_handlers.handle_search(["tag1", "tag2", "tag3"], "", None)
        self.assertEqual('{"success": "true", '
                         '"results": [' + str(self.ids[0]) + ", " + str(self.ids[1]) + ']}',
                         response.content.decode('utf-8'))

    def test_handle_abstract_page(self):
        response = view_handlers.handle_abstract_page("1", "http://localhost:8000/")
        self.assertEqual('{"success": "true", '
                         '"data": ['
                             '{"success": "true", '
                             '"article": {'
                                 '"id": "' + str(self.ids[0]) + '", ' 
                                 '"title": "Another Title", '
                                 '"abstract": "Another Abstract", '
                                 '"author": "Another Author", '
                                 '"date": "2019-06-07", '
                                 '"time_to_read": "456", '
                                 '"image": "http://localhost:8000/img/Blank.jpg", '
                                 '"tags": ["tag1", "tag3"]'
                             '}}, '
                             '{"success": "true", '
                             '"article": {'
                                 '"id": "' + str(self.ids[1]) + '", ' 
                                 '"title": "Title", '
                                 '"abstract": "Abstract", '
                                 '"author": "Author", '
                                 '"date": "2019-06-06", '
                                 '"time_to_read": "123", '
                                 '"image": "http://localhost:8000/img/Blank.jpg", '
                                 '"tags": ["tag1", "tag2"]'
                             '}}'
                         ']}',
                         response.content.decode('utf-8'))

    def test_handle_tags(self):
        response = view_handlers.handle_tags()
        self.assertEqual('{"success": "true", '
                         '"tags": ["tag1", "tag2", "tag3"]}',
                         response.content.decode('utf-8'))
