import datetime

from django.test import TestCase
from trends.db.obj.articleModel import Article, Tag
from trends import view_handlers

id = "0"

class ExampleTest(TestCase):
    def setUp(self):
        a = Article(title="Test Article",
                    author="John",
                    abstract="Testing testing testing",
                    body="Testing article article testing testing for article",
                    date=datetime.datetime.now(),
                    time_to_read=400000,
                    image="")
        a.save()
        id = a.pk
        Tag(tag="ArticleTest", article=a)

    def test_handle_latest_article_false(self):
        response = view_handlers.handle_latest_articles("2")
        self.assertEqual(b'{"success": "false"}', response.content)

    def test_handle_article_abstract_false(self):
        response = view_handlers.handle_article_abstract("1234")
        self.assertEqual(b'{"success":"false"}', response.content)

    def test_handle_article_data_false(self):
        response = view_handlers.handle_article_data("14")
        self.assertEqual(b'{"success":"false"}', response.content)

    def test_handle_article_edit_false(self):
        response = view_handlers.handle_article_edit("1234")
        self.assertEqual(b'{"success":"false"}', response.content)

    def test_handle_article_remove_false(self):
        current = str(datetime.datetime.now())
        response = view_handlers.handle_article_remove("1234", "Test Article", "John", "Testing testing", "Testing article", current, "400000", "")
        self.assertEqual(b'{"success":"false"}', response.content)

    # not too sure how to implement the list "latest" as jsonresponse
    def test_handle_latest_articles_exist(self):
        response = view_handlers.handle_latest_articles("1")
        articleList = []
        exampleArticle = Article(title="Test Article",
                                 author="John",
                                 abstract="Testing testing testing",
                                 body="Testing article article testing testing for article",
                                 date=datetime.datetime.now(),
                                 time_to_read=400000,
                                 image="")
        articleList.append(exampleArticle)
        self.assertEqual(b'{"success":"true", "latest": articleList', response.content)

    def test_handle_article_abstract_existing(self):
        response = view_handlers.handle_article_abstract(str(id))
        currentTime = str(datetime.datetime.now())
        self.assertEquals(
            b'{"success": "true", "article":{"title"="Test Article", "author":"John","abstract":"Testing testing testing","body":"Testing article article testing testing for article","date":currentTime,"time_to_read":"399999","image":""}',
            response.content())

    def test_handle_article_data(self):
        response = view_handlers.handle_article_data(str(id))
        currentTime = str(datetime.datetime.now())
        self.assertEquals(
            b'{"success": "true", "article":{"title"="Test Article", "author":"John","abstract":"Testing testing testing","body":"Testing article article testing testing for article","date":currentTime,"time_to_read":"400000","image":"","tags":"ArticleTest"}',
            response.content()
        )

    def test_handle_search(self):
        response = view_handlers.handle_search("ArticleTest", "Test", "1")
        articleList = []
        exampleArticle = Article(title="Test Article",
                                    author="John",
                                    abstract="Testing testing testing",
                                    body="Testing article article testing testing for article",
                                    date=datetime.datetime.now(),
                                    time_to_read=400000,
                                    image="")
        articleList.append(exampleArticle)
        self.assertEquals(
            b'{"success": "true", "results" : exampleArticle}', response.content
        )

    def test_handle_abstract_page(self):
        response = view_handlers.handle_abstract_page(1)
        articleList = []
        exampleArticle = Article(title="Test Article",
                                 author="John",
                                 abstract="Testing testing testing",
                                 body="Testing article article testing testing for article",
                                 date=datetime.datetime.now(),
                                 time_to_read=400000,
                                 image="",
                                 tags="ArticleTest")
        articleList.append(exampleArticle)
        self.assertEquals(
            b'{"success": "true", "results" : exampleArticle}', response.content
        )

    # Check if there is a way to confirm creation of certain file.
    def test_handle_article_new(self):
        current = datetime.now()
        response = view_handlers.handle_article_new("New article", "Doe", "tests", "bodypara", str(current), "")
        self.assertEqual('b{"success":"true"}')

    # def handle_article_edit(self):

    def test_handle_article_remove(self):
        response = view_handlers.handle_article_remove(id)
        self.assertEqual(b'{"success":"true"}', response.content )