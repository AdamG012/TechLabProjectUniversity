import datetime

from django.test import TestCase
from trends.db.obj.articleModel import Article, Tag
from trends import view_handlers


class ExampleTest(TestCase):
    def setUp(self):
        a = Article(title="Test Article Title",
                    author="Blip",
                    abstract="This is how you test",
                    body="1234567890qwertyuiopasdfghjklzxcvbnm",
                    date=datetime.datetime.now(),
                    time_to_read=400000,
                    image="")
        a.save()

        Tag(tag="Meme", article=a)

    def test_example(self):
        # FOR CONSISTENCY, ALL view_handlers METHODS TAKE ONLY STRINGS AS PARAMETERS

        response = view_handlers.handle_latest_articles("2")
        self.assertEqual(b'{"success": "false"}', response.content)
