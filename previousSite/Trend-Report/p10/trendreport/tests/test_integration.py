from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test import tag
from trendreport.models import Admin, Score, Trend, Project, Principle, AudienceMember
from taggit.managers import TaggableManager
from taggit.models import Tag

### INTEGRATION TESTS ###

# The integration tests included are designed to test combined elements including the database interactions.

# To run tests:
#    For all tests: 'py manage.py test trendreport'
#    To filter tests by their tags (say you want to run just the integration tests): 'py manage.py test trendreport --tag=integration'
#    NB: Tags for tests can be found above the test function eg @tag('integration', 'admin') and multiple tags can be specified on the command line as needed


# --------------- MODEL TESTS ---------------- #

# Test the __str__ return methods of all models
class TestModelStr(TestCase):

    @tag('integration', 'model')
    def test_audience_member_model_str(self):
        audience_member = AudienceMember(name='Test audience name')
        self.assertEquals(str(audience_member), 'Test audience name')

    @tag('integration', 'model')
    def test_principle_model_str(self):
        principle = Principle(name='Test principle name')
        self.assertEquals(str(principle), 'Test principle name')

    @tag('integration', 'model')
    def test_project_model_str(self):
        project = Project(name='Test project name')
        self.assertEquals(str(project), 'Test project name')

    @tag('integration', 'model')
    def test_trend_model_str(self):
        trend = Trend(name='Test trend name')
        self.assertEquals(str(trend), 'Test trend name')

    @tag('integration', 'model')
    def test_score_model_str(self):
        score = Score(score=5)
        self.assertEquals(str(score), 'Audience Member')

    @tag('integration', 'model')
    def test_admin_model_str(self):
        admin = Admin(name="The ICT Techlab")
        self.assertEquals(str(admin), 'Main Admin')


# --------------- ADMIN TESTS ---------------- #

# Test admin access for the admin panel
class TestAdminPanelAccess(TestCase):

    def create_admin_user(self):
        self.username = 'test_admin'
        self.email = 'test@test.com'
        self.password = '12345678'
        self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.is_active = True
        self.user.save()

    # Integration test - test admin login
    @tag('integration', 'admin')
    def test_admin_login(self):
        self.create_admin_user()
        logged_in = self.client.login(username=self.username, password=self.password)

        # Assert the super user is logged in to the current session
        self.assertTrue(logged_in)

    # Integration test - test admin access to the admin panel with active superuser - login page
    @tag('integration', 'admin')
    def test_admin_access_to_admin_login_page_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/login/?next=/admin/')
        self.assertRedirects(response, '/admin/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - main admin page
    @tag('integration', 'admin')
    def test_admin_access_to_main_admin_page_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_subpage_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/trendreport/')
        self.assertEquals(response.status_code, 200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport/admin subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_admin_subpage_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/trendreport/admin/')
        self.assertEquals(response.status_code, 200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport/audiencemember subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_audience_subpage_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/trendreport/audiencemember/')
        self.assertEquals(response.status_code, 200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport/principle subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_principle_subpage_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/trendreport/principle/')
        self.assertEquals(response.status_code, 200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport/project subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_project_subpage_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/trendreport/project/')
        self.assertEquals(response.status_code, 200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport/trend subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_trend_subpage_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/trendreport/trend/')
        self.assertEquals(response.status_code, 200)

    # Integration test - test admin access to the admin panel with active superuser - taggit subpage
    @tag('integration', 'admin')
    def test_admin_access_to_taggit_subpage_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/taggit/')
        self.assertEquals(response.status_code, 200)

    # Integration test - test admin access to the admin panel with active superuser - taggit/tag/ subpage
    @tag('integration', 'admin')
    def test_admin_access_to_taggit_tag_subpage_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/taggit/tag/')
        self.assertEquals(response.status_code, 200)

    # Integration test - test admin access to the admin panel with active superuser - password_change subpage
    @tag('integration', 'admin')
    def test_admin_access_to_taggit_subpage_url_with_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/admin/password_change/')
        self.assertEquals(response.status_code, 200)

    # Integration test - test admin access to the admin panel with inactive superuser - login page
    @tag('integration', 'admin')
    def test_admin_access_to_admin_login_page_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/login/?next=/admin/')
        self.assertEquals(response.status_code, 200)
        #self.assertRedirects(response, '/admin/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - main admin page
    @tag('integration', 'admin')
    def test_admin_access_to_main_admin_page_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/')
        self.assertRedirects(response, '/admin/login/?next=/admin/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_subpage_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/trendreport/')
        self.assertRedirects(response, '/admin/login/?next=/admin/trendreport/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport/admin/ subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_admin_subpage_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/trendreport/admin/')
        self.assertRedirects(response, '/admin/login/?next=/admin/trendreport/admin/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport/audiencemember subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_audience_subpage_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/trendreport/audiencemember/')
        self.assertRedirects(response, '/admin/login/?next=/admin/trendreport/audiencemember/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport/principle subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_principle_subpage_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/trendreport/principle/')
        self.assertRedirects(response, '/admin/login/?next=/admin/trendreport/principle/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport/project subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_project_subpage_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/trendreport/project/')
        self.assertRedirects(response, '/admin/login/?next=/admin/trendreport/project/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - trendreport/trend/ subpage
    @tag('integration', 'admin')
    def test_admin_access_to_trendreport_trend_subpage_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/trendreport/trend/')
        self.assertRedirects(response, '/admin/login/?next=/admin/trendreport/trend/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - taggit subpage
    @tag('integration', 'admin')
    def test_admin_access_to_taggit_subpage_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/taggit/')
        self.assertRedirects(response, '/admin/login/?next=/admin/taggit/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - taggit/tag/ subpage
    @tag('integration', 'admin')
    def test_admin_access_to_taggit_tag_subpage_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/taggit/tag/')
        self.assertRedirects(response, '/admin/login/?next=/admin/taggit/tag/', status_code=302, target_status_code=200)

    # Integration test - test admin access to the admin panel with active superuser - password_change subpage
    @tag('integration', 'admin')
    def test_admin_access_to_password_change_subpage_url_without_login(self):
        self.create_admin_user()
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/admin/password_change/')
        self.assertRedirects(response, '/admin/login/?next=/admin/password_change/', status_code=302, target_status_code=200)


# --------------- VIEWS AND MODELS TESTS ---------------- #
class TestViewsAndModelsWithConnectedData(TestCase):

    # Create test data to populate the test database
    # Models (Admin, Principle, AudienceMember, Trend, Project, Score) map to database classes
    # Views display the contextual data retrieved from the database as html
    def create_models(self):

        # ----------------- TAG TEST DATA ----------------- #

        self.test_tag_1 = Tag(name='Test Tag 1')
        self.test_tag_1.save()
        self.test_tag_2 = Tag(name='Test Tag 2')
        self.test_tag_2.save()
        self.test_tag_3 = Tag(name='Test Tag 3')
        self.test_tag_3.save()

        # ----------------- ADMIN - ICT TECHLAB TEST DATA ----------------- #

        self.test_techlab = Admin(name='Test Techlab Name', tagline='Test Techlab Tagline', description='Test Techlab Description')
        self.test_techlab.save()


        # ----------------- AUDIENCE MEMBER TEST DATA ----------------- #

        self.test_audience_1 = AudienceMember(name='Test Audience Name 1')
        self.test_audience_1.save()
        self.test_audience_2 = AudienceMember(name='Test Audience Name 2')
        self.test_audience_2.save()
        self.test_audience_3 = AudienceMember(name='Test Audience Name 3')
        self.test_audience_3.save()


        # ----------------- PRINCIPLES TEST DATA -----------------#

        self.test_principle_1 = Principle(name='Test Principle Name 1', description='Test Principle Description 1', icon='info')
        self.test_principle_1.save()
        self.test_principle_2 = Principle(name='Test Principle Name 2', description='Test Principle Description 2', icon='flash')
        self.test_principle_2.save()
        self.test_principle_3 = Principle(name='Test Principle Name 3', description='Test Principle Description 3', icon='database')
        self.test_principle_3.save()


        # ----------------- PROJECTS TEST DATA ----------------- #

        self.test_project_1 = Project(name='Test Project Name 1', description='Test Project Description 1',
                                      short_description='Test Project Short Desc 1')
        self.test_project_1.save()
        self.test_project_1.principles=[self.test_principle_1]
        self.test_project_1.tags.add(self.test_tag_1)
        self.test_project_1.save()

        self.test_project_2 = Project(name='Test Project Name 2', description='Test Project Description 2',
                                      short_description='Test Project Short Desc 2')
        self.test_project_2.save()
        self.test_project_2.principles=[self.test_principle_2]
        self.test_project_2.tags.add(self.test_tag_2)
        self.test_project_2.save()

        self.test_project_3 = Project(name='Test Project Name 3', description='Test Project Description 3',
                                      short_description='Test Project Short Desc 3')
        self.test_project_3.save()
        self.test_project_3.principles=[self.test_principle_3]
        self.test_project_3.tags.add(self.test_tag_3)
        self.test_project_3.save()

        self.test_project_1.projects=[self.test_project_2, self.test_project_3]
        self.test_project_1.save()
        self.test_project_2.projects=[self.test_project_1, self.test_project_3]
        self.test_project_2.save()
        self.test_project_3.projects=[self.test_project_1, self.test_project_2]
        self.test_project_3.save()


        # ----------------- TRENDS TEST DATA ----------------- #

        self.test_trend_1 = Trend(name='Test Trend Name 1', description='Test Trend Description 1',
                                  short_description='Test Trend Short Desc 1', importance='Test Trend Importance 1',
                                  howToProceed='Test Trend How To Proceed 1', examples='Test Trend Example 1')
        self.test_trend_1.save()
        self.test_trend_1.projects=[self.test_project_1, self.test_project_2]
        self.test_trend_1.principles=[self.test_principle_1, self.test_principle_2]
        self.test_trend_1.tags.add(self.test_tag_1)
        self.test_trend_1.save()

        self.test_trend_2 = Trend(name='Test Trend Name 2', description='Test Trend Description 2',
                                  short_description='Test Trend Short Desc 2', importance='Test Trend Importance 2',
                                  howToProceed='Test Trend How To Proceed 2', examples='Test Trend Example 2')
        self.test_trend_2.save()
        self.test_trend_2.projects = [self.test_project_2, self.test_project_3]
        self.test_trend_2.principles = [self.test_principle_2, self.test_principle_3]
        self.test_trend_2.tags.add(self.test_tag_2)
        self.test_trend_2.save()

        self.test_trend_3 = Trend(name='Test Trend Name 3', description='Test Trend Description 3',
                                  short_description='Test Trend Short Desc 3', importance='Test Trend Importance 3',
                                  howToProceed='Test Trend How To Proceed 3', examples='Test Trend Example 3')
        self.test_trend_3.save()
        self.test_trend_3.projects = [self.test_project_1, self.test_project_3]
        self.test_trend_3.principles = [self.test_principle_1, self.test_principle_3]
        self.test_trend_3.tags.add(self.test_tag_3)
        self.test_trend_3.save()


        # ----------------- SCORES TEST DATA ----------------- #

        self.test_score_1 = Score(trend=self.test_trend_1, audienceMember=self.test_audience_1, score=2)
        self.test_score_1.save()
        self.test_score_2 = Score(trend=self.test_trend_2, audienceMember=self.test_audience_2, score=5)
        self.test_score_2.save()
        self.test_score_3 = Score(trend=self.test_trend_3, audienceMember=self.test_audience_3, score=8)
        self.test_score_3.save()

    # Delete the data from the test database after test complete
    def delete_test_data(self):
        self.test_techlab.delete()
        self.test_audience_1.delete()
        self.test_audience_2.delete()
        self.test_audience_3.delete()
        self.test_principle_1.delete()
        self.test_principle_2.delete()
        self.test_principle_3.delete()
        self.test_project_1.delete()
        self.test_project_2.delete()
        self.test_project_3.delete()
        self.test_trend_1.delete()
        self.test_trend_2.delete()
        self.test_trend_3.delete()
        self.test_score_1.delete()
        self.test_score_2.delete()
        self.test_score_3.delete()

    #
    ### PRINCIPLES PAGE ###
    #

    # Integration test - check the name of principle 1 is displayed on the principles page
    @tag('integration', 'views', 'models')
    def test_principle_view_with_principle_1_name(self):
        self.create_models()
        response = self.client.get('/principles/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_1.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the name of principle 2 is displayed on the principles page
    @tag('integration', 'views', 'models')
    def test_principle_view_with_principle_2_name(self):
        self.create_models()
        response = self.client.get('/principles/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_2.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the name of principle 3 is displayed on the principles page
    @tag('integration', 'views', 'models')
    def test_principle_view_with_principle_3_name(self):
        self.create_models()
        response = self.client.get('/principles/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the description of principle 1 is displayed on the principles page
    @tag('integration', 'views', 'models')
    def test_principle_view_with_principle_1_description(self):
        self.create_models()
        response = self.client.get('/principles/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_1.description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the description of principle 2 is displayed on the principles page
    @tag('integration', 'views', 'models')
    def test_principle_view_with_principle_2_description(self):
        self.create_models()
        response = self.client.get('/principles/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_2.description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the description of principle 3 is displayed on the principles page
    @tag('integration', 'views', 'models')
    def test_principle_view_with_principle_3_description(self):
        self.create_models()
        response = self.client.get('/principles/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_3.description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the icon of principle 1 is displayed on the principles page
    @tag('integration', 'views', 'models')
    def test_principle_view_with_principle_1_icon(self):
        self.create_models()
        response = self.client.get('/principles/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_1.icon, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the icon of principle 2 is displayed on the principles page
    @tag('integration', 'views', 'models')
    def test_principle_view_with_principle_2_icon(self):
        self.create_models()
        response = self.client.get('/principles/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_2.icon, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the icon of principle 3 is displayed on the principles page
    @tag('integration', 'views', 'models')
    def test_principle_view_with_principle_3_icon(self):
        self.create_models()
        response = self.client.get('/principles/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_3.icon, response.content.decode('utf8'))
        self.delete_test_data()


    #
    ### ICT TECHLAB PAGE ###
    #


    # Integration test - check the name of the ICT Techlab 'Admin' model is displayed on the ICT Techlab page
    @tag('integration', 'views', 'models')
    def test_icttechlab_view_name(self):
        self.create_models()
        response = self.client.get('/icttechlab/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_techlab.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the tagline of the ICT Techlab 'Admin' model is displayed on the ICT Techlab page
    @tag('integration', 'views', 'models')
    def test_icttechlab_view_tagline(self):
        self.create_models()
        response = self.client.get('/icttechlab/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_techlab.tagline, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the description of the ICT Techlab 'Admin' model is displayed on the ICT Techlab page
    @tag('integration', 'views', 'models')
    def test_icttechlab_view_description(self):
        self.create_models()
        response = self.client.get('/icttechlab/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_techlab.description, response.content.decode('utf8'))
        self.delete_test_data()


    #
    ### TREND INDEX PAGE ###
    #


    # Integration test - check the name of the audience 1 appears on the trend index page
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_index_page_view_with_audience_1_name(self):
        self.create_models()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_audience_1.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the name of the audience 2 appears on the trend index page
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_index_page_view_with_audience_2_name(self):
        self.create_models()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_audience_2.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the name of the audience 3 appears on the trend index page
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_index_page_view_with_audience_3_name(self):
        self.create_models()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_audience_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the name of the trend 1 appears on the trend index page
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_index_page_view_with_trend_1_name(self):
        self.create_models()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - check the name of the trend 2 appears on the trend index page
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_index_page_view_with_trend_2_name(self):
        self.create_models()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - check the name of the trend 3 appears on the trend index page
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_index_page_view_with_trend_3_name(self):
        self.create_models()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the short description of the trend 1 appears on the trend index page
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_index_page_view_with_trend_1_short_description(self):
        self.create_models()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.short_description, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - check the short description of the trend 2 appears on the trend index page
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_index_page_view_with_trend_2_short_description(self):
        self.create_models()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_2.short_description, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - check the short description of the trend 3 appears on the trend index page
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_index_page_view_with_trend_3_short_description(self):
        self.create_models()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_3.short_description, response.content.decode('utf8'))
        self.delete_test_data()


    #
    ### TREND PAGE ###
    #


    # Integration test - check the name of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_1_name(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the name of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_2_name(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the name of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_3_name(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the description of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_1_description(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the description of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_2_description(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_2.description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the description of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_3_description(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_3.description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the importance of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_1_importance(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.importance, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the importance of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_2_importance(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_2.importance, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the importance of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_3_importance(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_3.importance, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the howToProceed of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_1_howToProceed(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.howToProceed, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the howToProceed of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_2_howToProceed(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_2.howToProceed, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the howToProceed of a trend shows on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_3_howToProceed(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_3.howToProceed, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the names of related projects of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_1_related_projects_names(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Projects', response.content.decode('utf8'))
        self.assertIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_2.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the names of related projects of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_2_related_projects_names(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Projects', response.content.decode('utf8'))
        self.assertIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the names of related projects of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_3_related_projects_names(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Projects', response.content.decode('utf8'))
        self.assertIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the short descriptions of related projects of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_1_related_projects_short_descriptions(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_project_1.short_description, response.content.decode('utf8'))
        self.assertIn(self.test_project_2.short_description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the short descriptions of related projects of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_2_related_projects_short_descriptions(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_project_2.short_description, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.short_description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the short descriptions of related projects of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_3_related_projects_short_descriptions(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_project_1.short_description, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.short_description, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - check the icons of principles of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_1_principles_icons(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_1.icon, response.content.decode('utf8'))
        self.assertIn(self.test_principle_2.icon, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - check the icons of principles of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_2_principles_icons(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_2.icon, response.content.decode('utf8'))
        self.assertIn(self.test_principle_3.icon, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the icons of principles of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_3_principles_icons(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_1.icon, response.content.decode('utf8'))
        self.assertIn(self.test_principle_3.icon, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the tags of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_1_tag(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Test Tag 1', response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the tags of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_2_tag(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Test Tag 2', response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the tags of a trend show on a specific trend page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_trend_page_view_with_trend_3_tag(self):
        self.create_models()
        response = self.client.get('/trend/%d' % self.test_trend_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Test Tag 3', response.content.decode('utf8'))
        self.delete_test_data()



    #
    ### PROJECT PAGE ###
    #

    # Integration test - check the name of a project shows on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_1_name(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_project_1.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the name of a project shows on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_2_name(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_project_2.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the name of a project shows on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_3_name(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the description of a project shows on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_1_description(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_project_1.description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the description of a project shows on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_2_description(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_project_2.description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the description of a project shows on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_3_description(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_project_3.description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the names of related trends of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_1_related_trend_names(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Related Trends', response.content.decode('utf8'))
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the names of related trends of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_2_related_trend_names(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Related Trends', response.content.decode('utf8'))
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the names of related trends of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_3_related_trend_names(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Related Trends', response.content.decode('utf8'))
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the short description of related trends of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_1_related_trend_short_description(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.short_description, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.short_description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the short description of related trends of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_2_related_trend_short_description(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.short_description, response.content.decode('utf8'))
        self.assertIn(self.test_trend_2.short_description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the short description of related trends of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_3_related_trend_short_description(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_2.short_description, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.short_description, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - check the names of related projects of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_1_related_projects_names(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Related Projects', response.content.decode('utf8'))
        self.assertIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the names of related projects of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_2_related_projects_names(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Related Projects', response.content.decode('utf8'))
        self.assertIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the names of related projects of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_3_related_projects_names(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Related Projects', response.content.decode('utf8'))
        self.assertIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_2.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the short description of related projects of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_1_related_projects_short_description(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Related Projects', response.content.decode('utf8'))
        self.assertIn(self.test_project_2.short_description, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.short_description, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - check the short description of related projects of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_2_related_projects_short_description(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Related Projects', response.content.decode('utf8'))
        self.assertIn(self.test_project_1.short_description, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.short_description, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - check the short description of related projects of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_3_related_projects_short_description(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Related Projects', response.content.decode('utf8'))
        self.assertIn(self.test_project_1.short_description, response.content.decode('utf8'))
        self.assertIn(self.test_project_2.short_description, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the icon of a principle of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_1_principles_icons(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_1.icon, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the icon of a principle of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_2_principles_icons(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_2.icon, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the icon of a principle of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_3_principles_icons(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_principle_3.icon, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the tags of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_1_tag(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Test Tag 1', response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the tags of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_2_tag(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_2.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Test Tag 2', response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - check the tags of a project show on a specific project page by pk
    @tag('integration', 'views', 'models', 'realdata')
    def test_project_page_view_with_project_3_tag(self):
        self.create_models()
        response = self.client.get('/project/%d' % self.test_project_3.pk)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Test Tag 3', response.content.decode('utf8'))
        self.delete_test_data()


    #
    ### SEARCH PAGE ###
    #

    # Integration test - test the search function with search term to return all trends/ projects
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_test_term_all_trends_all_projects(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with search term to return all trends only
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_test_term_all_trends_only(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with trend name 1
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_name_1(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+Name+%d' % 1)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with trend name 2
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_name_2(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+Name+%d' % 2)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with trend name 3
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_name_3(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+Name+%d' % 3)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - test the search function with trend description 1
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_description_1(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+Description+%d' % 1)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with trend description 2
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_description_2(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+Description+%d' % 2)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with trend description 3
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_description_3(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+Description+%d' % 3)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - test the search function with trend importance 1
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_importance_1(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+Importance+%d' % 1)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with trend importance 2
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_importance_2(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+Importance+%d' % 2)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with trend importance 3
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_importance_3(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+Importance+%d' % 3)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with trend howToProceed 1
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_howToProceed_1(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+How+To+Proceed+%d' % 1)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with trend howToProceed 2
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_howToProceed_2(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+How+To+Proceed+%d' % 2)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with trend howToProceed 3
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_trend_howToProceed_3(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Trend+How+To+Proceed+%d' % 3)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with tag 1
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_test_tag_1(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Tag+%d' % 1)
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with tag 2
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_test_tag_2(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Tag+%d' % 2)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with tag 3
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_test_tag_3(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Tag+%d' % 3)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()



    # Integration test - test the search function with search term to return all projects only
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_test_term_all_projects_only(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Project')
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()


    # Integration test - test the search function with project name 1
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_project_name_1(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Project+Name+%d' % 1)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with project name 2
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_project_name_2(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Project+Name+%d' % 2)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with project name 3
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_project_name_3(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Project+Name+%d' % 3)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with project description 1
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_project_description_1(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Project+Description+%d' % 1)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with project description 2
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_project_description_2(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Project+Description+%d' % 2)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()

    # Integration test - test the search function with project description 3
    @tag('integration', 'views', 'models', 'realdata')
    def test_search_page_view_with_project_description_3(self):
        self.create_models()
        response = self.client.get('/search-results/?q=Test+Project+Description+%d' % 3)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn(self.test_trend_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_2.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_trend_3.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_1.name, response.content.decode('utf8'))
        self.assertNotIn(self.test_project_2.name, response.content.decode('utf8'))
        self.assertIn(self.test_project_3.name, response.content.decode('utf8'))
        self.delete_test_data()