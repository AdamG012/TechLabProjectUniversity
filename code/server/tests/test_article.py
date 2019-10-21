import datetime

from django.test import TestCase
from trends.db.obj.articleModel import Article, Tag
from trends import view_handlers



class ArticleTest(TestCase):
    def setUp(self):
        self.currentTime = datetime.datetime.now()

        a = Article(title="Test Article",
                    author="John",
                    abstract="Testing testing testing",
                    body="Testing article article testing testing for article",
                    date=currentTime,
                    time_to_read="400000",
                    image="")
        a.save()
        self.id = a.pk
        Tag(tag="ArticleTest", article=a)

    def test_handle_latest_article_false(self):
        response = view_handlers.handle_latest_articles("2")
        self.assertEqual(b'{"success": "false"}', response.content)

    def test_handle_article_abstract_false(self):
        response = view_handlers.handle_article_abstract("1234")
        self.assertEqual(b'{"success": "false"}', response.content)

    def test_handle_article_data_false(self):
        response = view_handlers.handle_article_data("14")
        self.assertEqual(b'{"success": "false"}', response.content)

    def test_handle_article_edit_false(self):
        response = view_handlers.handle_article_edit("1234", "Test Article", "John", "Testing testing", "Testing article", self.currentTime, "400000", "")
        self.assertEqual(b'{"success": "false"}', response.content)

    def test_handle_article_remove_false(self):
        response = view_handlers.handle_article_remove("14")
        self.assertEqual(b'{"success": "false"}', response.content)

    # not too sure how to implement the list "latest" as jsonresponse
    def test_handle_latest_articles_exist(self):
        response = view_handlers.handle_latest_articles(self.id)
        articleList = []
        exampleArticle = Article(title="Test Article",
                                 author="John",
                                 abstract="Testing testing testing",
                                 body="Testing article article testing testing for article",
                                 date=self.currentTime,
                                 time_to_read="400000",
                                 image="")
        articleList.append(exampleArticle)
        self.assertEqual(b'{"success": "true", "latest": ' + str(articleList) + '}', response.content)

    def test_handle_article_abstract_existing(self):
        response = view_handlers.handle_article_abstract(self.id)
        self.assertEquals(
            b'{"success": "true", 
                "article":{"title": "Test Article", 
                            "author": "John",
                            "abstract": "Testing testing testing",
                            "body": "Testing article article testing testing for article",
                            "date": str(self.currentTime),
                            "time_to_read": "399999",
                            "image": ""}',
            response.content()
        )

    def test_handle_article_data(self):
        response = view_handlers.handle_article_data(self.id)
        self.assertEquals(
            b'{"success": "true",
                    "article":{"title": "Test Article", 
                                "author": "John",
                                "abstract": "Testing testing testing",
                                "body": "Testing article article testing testing for article",
                                "date": str(self.currentTime),
                                "time_to_read": "400000",
                                "image": "",
                                "tags": "ArticleTest"}',
            response.content()
        )

    def test_handle_search(self):
        response = view_handlers.handle_search("ArticleTest", "Test", "1")
        articleList = []
        exampleArticle = Article(title="Test Article",
                                    author="John",
                                    abstract="Testing testing testing",
                                    body="Testing article article testing testing for article",
                                    date=self.currentTime,
                                    time_to_read="400000",
                                    image="")
        articleList.append(exampleArticle)
        self.assertEquals(b'{"success": "true", "results": ' + str(articleList) + '}', response.content)

    def test_handle_abstract_page(self):
        response = view_handlers.handle_abstract_page("1")
        articleList = []
        exampleArticle = Article(title="Test Article",
                                 author="John",
                                 abstract="Testing testing testing",
                                 body="Testing article article testing testing for article",
                                 date=self.currentTime,
                                 time_to_read="400000",
                                 image="",
                                 tags="ArticleTest")
        articleList.append(exampleArticle)
        self.assertEquals(
            b'{"success": "true", "results": '+ str(articleList) + '}', response.content
        )

   
    def test_handle_article_new(self):
        response = view_handlers.handle_article_new("New article", "Doe", "tests", "bodypara", str(current), "")
        self.assertEqual('b{"success": "true"}', response.content)

    def handle_article_edit(self):
        newTime = datetime.datetime.now()
        response = view_handlers.handle_article_edit(self.id, "Test Article", "Jim", "Tested", "bodypara", str(newTime), "10", "")
        self.assertEqual('b{"success": "true"}', response.content)

    def test_handle_article_remove(self):
        response = view_handlers.handle_article_remove(self.id)
        self.assertEqual(b'{"success": "true"}', response.content)