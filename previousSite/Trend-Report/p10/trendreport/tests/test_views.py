from django.test import RequestFactory
from django.core.urlresolvers import reverse
from unittest.mock import patch, MagicMock, NonCallableMock
from unittest import TestCase
from django.test import TestCase, Client
from trendreport.views import trends_index, custom_404_page, custom_500_page, trend_page, project_page, principles_page, icttechlab_page
from django.test import tag
from trendreport.models import Admin, Score, Trend, Project, Principle, AudienceMember, BaseModel

### VIEWS UNIT TESTS ###

# Unit testing the views with an entry into the database to assist in rendering the context/html response
# To run tests:
#    For all tests: 'py manage.py test trendreport'
#    To filter tests by their tags (say you want to run just the unit tests): 'py manage.py test trendreport --tag=unit'
#    NB: Tags for tests can be found above the test function eg @tag('unit')


# Unit tests for the Trend Index View
class TestTrendIndexView(TestCase):

    # Set up the request factory for the whole class
    @classmethod
    def setUp(cls):
        cls.factory = RequestFactory()
        cls.request = cls.factory.get('/trends_index')
        cls.response = trends_index(cls.request)

    # Unit test the <URL>/trends_index returns a 200 status_code when requested
    @tag('unit', 'views')
    def test_trend_index_view_status(self):
        self.assertEqual(self.response.status_code, 200)

    # Unit test <URL>/trends_index uses the trend-list.html template
    @tag('unit', 'views')
    def test_trend_index_view_template(self):
        self.assertTemplateUsed('trend-list.html')

    # Unit test <URL>/trends_index displays hardcoded title from html
    @tag('unit', 'views')
    def test_trend_index_view_display(self):
        html = self.response.content.decode('utf8')
        self.assertIn('Trends', html)


# Unit tests for the Trend Page View
class TestTrendPageView(TestCase):

    # Unit test the <URL>/trends/# returns a 200 status_code when requested, no redirect
    @tag('unit', 'views')
    def test_trend_page_view_status(self):
        test_trend = Trend(name='Test Trend Name', description='Test Trend Description', importance='', howToProceed='')
        test_trend.save()
        response = self.client.get('/trend/%d' % test_trend.pk)
        self.assertEqual(response.status_code, 200)

    # Unit test <URL>/trend/# uses the trend.html template
    @tag('unit', 'views')
    def test_trend_page_view_template(self):
        test_trend = Trend(name='Test Trend Name', description='Test Trend Description', importance='', howToProceed='')
        test_trend.save()
        response = self.client.get('/trend/%d' % test_trend.pk, follow=True)
        self.assertTemplateUsed('trend.html')

    # Unit test <URL>/trend/# displays hardcoded title from html
    @tag('unit', 'views')
    def test_trend_page_view_display(self):
        test_trend = Trend(name='Test Trend Name', description='Test Trend Description', importance='', howToProceed='')
        test_trend.save()
        response = self.client.get('/trend/%d' % test_trend.pk, follow=True)
        html = response.content.decode('utf8')
        self.assertIn('Test Trend Name', html)


# Unit tests for the Project Page View
class TestProjectPageView(TestCase):

    # Unit test the <URL>/project/# returns a 200 status_code when requested, no redirect
    @tag('unit', 'views')
    def test_project_page_view_status(self):
        test_project = Project(name='Test Project Name', description='Test Project Description')
        test_project.save()
        response = self.client.get('/project/%d' % test_project.pk)
        self.assertEqual(response.status_code, 200)

    # Unit test <URL>/project/# uses the project.html template
    @tag('unit', 'views')
    def test_project_page_view_template(self):
        test_project = Project(name='Test Project Name', description='Test Project Description')
        test_project.save()
        response = self.client.get('/project/%d' % test_project.pk)
        self.assertTemplateUsed('project.html')

    # Unit test <URL>/project/# displays hardcoded title from html
    @tag('unit', 'views')
    def test_project_page_view_display(self):
        test_project = Project(name='Test Project Name', description='Test Project Description')
        test_project.save()
        response = self.client.get('/project/%d' % test_project.pk)
        html = response.content.decode('utf8')
        self.assertIn('Test Project Name', html)

# Unit tests for the Principles View
class TestPrinciplesPageView(TestCase):


    # Unit test the <URL>/principles returns a 301 status_code when requested, no redirect
    @tag('unit', 'views')
    def test_principles_page_view_status_before_redirect(self):
        test_principle = Principle(name='Test Principle Name', description='Test Principle Description')
        test_principle.save()
        response = self.client.get('/principles', follow=False)
        self.assertEqual(response.status_code, 301)

    # Unit test the <URL>/principles returns a 200 status_code when requested, after redirect
    @tag('unit', 'views')
    def test_principles_page_view_status_after_redirect(self):
        test_principle = Principle(name='Test Principle Name', description='Test Principle Description')
        test_principle.save()
        response = self.client.get('/principles', follow=True)
        self.assertEqual(response.status_code, 200)

    # Unit test <URL>/principles uses the principles.html template
    @tag('unit', 'views')
    def test_principles_page_view_template(self):
        test_principle = Principle(name='Test Principle Name', description='Test Principle Description')
        test_principle.save()
        response = self.client.get('/principles', follow=True)
        self.assertTemplateUsed('principles.html')

    # Unit test <URL>/principles displays hardcoded title from html
    @tag('unit', 'views')
    def test_principles_page_view_display(self):
        test_principle = Principle(name='Test Principle Name', description='Test Principle Description')
        test_principle.save()
        response = self.client.get('/principles', follow=True)
        html = response.content.decode('utf8')
        self.assertIn('Digital Principles', html)


# Unit tests for the ICT Techlab View
class TestICTTechlabView(TestCase):

    # Unit test the <URL>/icttechlab returns a 301 status_code when requested, no redirect
    @tag('unit', 'views')
    def test_ict_techlab_page_view_status_before_redirect(self):
        test_techlab = Admin(name='ICT Techlab', description='Techlab description test.')
        test_techlab.save()
        response = self.client.get('/icttechlab', follow=False)
        self.assertEqual(response.status_code, 301)

    # Unit test the <URL>/icttechlab returns a 200 status_code when requested, after redirect
    @tag('unit', 'views')
    def test_ict_techlab_page_view_status_after_redirect(self):
        test_techlab = Admin(name='ICT Techlab', description='Techlab description test.')
        test_techlab.save()
        response = self.client.get('/icttechlab', follow=True)
        self.assertEqual(response.status_code, 200)

    # Unit test <URL>/icttechlab uses the ict-techlab.html template
    @tag('unit', 'views')
    def test_ict_techlab_page_view_template(self):
        test_techlab = Admin(name='ICT Techlab', description='Techlab description test.')
        test_techlab.save()
        response = self.client.get('/icttechlab', follow=True)
        self.assertTemplateUsed('ict-techlab.html')

    # Unit test <URL>/icttechlab displays hardcoded title from html
    @tag('unit', 'views')
    def test_ict_techlab_page_view_display(self):
        test_techlab = Admin(name='Test ICT Techlab', description='Techlab description test.')
        test_techlab.save()
        response = self.client.get('/icttechlab', follow=True)
        html = response.content.decode('utf8')
        self.assertIn('The ICT Techlab', html)


# Unit tests for the 404 and 500 View
class TestErrorStatusView(TestCase):

    # Unit test <URL>/<PARAM DOES NOT EXIST>
    @tag('unit', 'views')
    def test_404_page_view_template(self):
        factory = RequestFactory()
        request = factory.get('/linkdoesnotexist')
        response = custom_404_page(request)
        self.assertTemplateUsed('custom_404.html')

    # Unit test <URL>/<INTERNAL SERVER ERROR>
    @tag('unit', 'views')
    def test_500_page_view_template(self):
        factory = RequestFactory()
        request = factory.get('/linkdoesnotexist')
        response = custom_500_page(request)
        self.assertTemplateUsed('custom_500.html')

