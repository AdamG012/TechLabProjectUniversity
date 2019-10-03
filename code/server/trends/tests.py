from django.test import TestCase, tag
from .admin_views import *


#                       Article Test

# - Testing functionality of get articles, queries, and tagging functionality
# - Determining functionality for proper routing and retrieval of articles.

# - To run all these tests use:
#       python manage.py test server
# - To run these tests specifically as unit tests e.g. run by tag.
#       python manage.py test server --tag=unit

class ArticleTest(TestCase):

    @tag('unit', 'article')
    def test_get_article_none(self):
        self.assertIsNone(get_article(None))

    @tag('unit', 'article')
    def test_get_article_not_found(self):
        self.assertIsNone(get_article(21481241294718718))
