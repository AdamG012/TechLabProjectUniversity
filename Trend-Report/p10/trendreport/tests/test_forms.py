from trendreport.models import Admin, Score, Trend, Project, Principle, AudienceMember, BaseModel
from trendreport.forms import AudienceMemberForm, PrincipleForm, TrendForm, ProjectForm
from unittest import TestCase
from mock import MagicMock
from django.test import tag
from django import forms
from django.forms import CheckboxSelectMultiple, inlineformset_factory, TextInput
from ckeditor_uploader.widgets import CKEditorUploadingWidget


### FORMS UNIT TESTS ###

# Unit testing the model forms to check for correct input types
# These tests are intended to isolate the view functions without engaging with the database
# To run tests:
#    For all tests: 'py manage.py test trendreport'
#    To filter tests by their tags (say you want to run just the unit tests): 'py manage.py test trendreport --tag=unit'
#    NB: Tags for tests can be found above the test function eg @tag('unit')


# Unit tests for the AudienceMemberForm
class TestAudienceMemberForm(TestCase):

    # Set up the form instance for the class
    @classmethod
    def setUp(cls):
        cls.form = AudienceMemberForm()

    # Unit test existence of the name field in the Audience Member Form
    @tag('unit', 'forms')
    def test_audience_member_form_name_field(self):
        self.assertIn('name="name"', self.form.as_p())

    # Unit test Audience Member Form has fields to populate
    @tag('unit', 'forms')
    def test_audience_member_form_has_one_field(self):
        self.assertEqual(1, len(self.form.fields))

    # Unit test for validation of empty form - empty form invalid
    @tag('unit', 'forms')
    def test_audience_member_form_validation_for_no_input_provided(self):
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new empty name field - empty field invalid
    @tag('unit', 'forms')
    def test_audience_member_form_validation_for_empty_field(self):
        self.form = AudienceMemberForm(data={'name': ""})
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new non-empty field that's too long - field invalid, max length 50
    @tag('unit', 'forms')
    def test_audience_member_form_validation_for_field_over_max_length(self):
        self.form = AudienceMemberForm(data={'name': "The name field cannot be longer than 50 characters and this is longer than expected."})
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new non-empty field under the max length - form valid
    @tag('unit', 'forms')
    def test_audience_member_form_validation_for_field_under_max_length(self):
        self.form = AudienceMemberForm(data={'name': "Student"})
        self.assertTrue(self.form.is_valid())


# Unit tests for the PrincipleForm
class TestPrincipleForm(TestCase):

    # Set up the form instance for the class
    @classmethod
    def setUp(cls):
        cls.form = PrincipleForm()

    # Unit test existence of the name field in the Principle Form
    @tag('unit', 'forms')
    def test_principle_form_name_field(self):
        self.assertIn('name="name"', self.form.as_p())

    # Unit test Principle Form has fields to populate
    @tag('unit', 'forms')
    def test_principle_form_has_three_fields(self):
        self.assertEqual(3, len(self.form.fields))

    # Unit test for validation of empty form - empty form invalid
    @tag('unit', 'forms')
    def test_principle_form_validation_for_no_input_provided(self):
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new empty name field - empty field invalid
    @tag('unit', 'forms')
    def test_principle_form_validation_for_empty_name_field(self):
        self.form = PrincipleForm(data={'name': "", 'description': "Description about the principle."})
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new empty description field - empty field invalid
    @tag('unit', 'forms')
    def test_principle_form_validation_for_empty_description_field(self):
        self.form = PrincipleForm(data={'name': "Mobile First", 'description': ""})
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new non-empty field that's too long - field invalid, max length 50
    @tag('unit', 'forms')
    def test_principle_form_validation_for_field_over_max_length(self):
        self.form = PrincipleForm(data={'name': "The name field cannot be longer than 50 characters and this is longer than expected.", 'description': "Description of the principle."})
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new non-empty field under the max length - form valid
    @tag('unit', 'forms')
    def test_principle_form_validation_for_field_under_max_length(self):
        self.form = PrincipleForm(data={'name': "Mobile First", 'description': "Description about the principle."})
        self.assertTrue(self.form.is_valid())


# Unit tests for the TrendForm
class TestTrendForm(TestCase):

    # Set up the form instance for the class
    @classmethod
    def setUp(cls):
        cls.form = TrendForm()

    # Unit test existence of the principles field in the Trend Form
    @tag('unit', 'forms')
    def test_trend_form_principles_field(self):
        self.assertIn('id="id_principles"', self.form.as_p())

    # Unit test existence of the projects field in the Trend Form
    @tag('unit', 'forms')
    def test_trend_form_projects_field(self):
        self.assertIn('id="id_projects"', self.form.as_p())

    # Unit test existence of the short description field in the Trend Form
    @tag('unit', 'forms')
    def test_trend_form_short_description_field(self):
        self.assertIn('name="short_description"', self.form.as_p())

    # Unit test existence of the short description field in the Trend Form
    @tag('unit', 'forms')
    def test_trend_form_name_field(self):
        self.assertIn('name="name"', self.form.as_p())

    # Unit test Trend Form has fields to populate
    @tag('unit', 'forms')
    def test_trend_form_has_eleven_fields(self):
        self.assertEqual(11, len(self.form.fields))

    # Unit test for validation of empty form - empty form invalid
    @tag('unit', 'forms')
    def test_trend_form_validation_for_no_input_provided(self):
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of empty fields - empty fields invalid
    @tag('unit', 'forms')
    def test_trend_form_validation_for_empty_fields(self):
        self.form = TrendForm(data={'name': "", 'description': "", 'importance': "", 'howToProceed': ""})
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of empty name field - empty name field invalid
    @tag('unit', 'forms')
    def test_trend_form_validation_for_empty_name_field(self):
        test_audience = AudienceMember(name='Student1')
        test_audience.save()
        self.form = TrendForm(data={'name': "", 'description': "Description for a trend", 'importance': "Importance of a trend", 'howToProceed': "How to proceed with a trend", 'rating':[test_audience.pk]})
        self.assertFalse(self.form.is_valid())
        test_audience.delete()

    # Unit test for validation of empty description field - empty description field invalid
    @tag('unit', 'forms')
    def test_trend_form_validation_for_empty_description_field(self):
        test_audience = AudienceMember(name='Student2')
        test_audience.save()
        self.form = TrendForm(data={'name': "Trend name", 'description': "", 'importance': "Importance of a trend", 'howToProceed': "How to proceed with a trend", 'ratings':[test_audience.pk]})
        self.assertFalse(self.form.is_valid())
        test_audience.delete()

    # Unit test for validation of empty importance field - empty importance field OK
    @tag('unit', 'forms')
    def test_trend_form_validation_for_empty_importance_field(self):
        test_audience = AudienceMember(name='Student3')
        test_audience.save()
        self.form = TrendForm(data={'name': "Trend name", 'description': "Description of a trend", 'importance': "", 'howToProceed': "How to proceed with a trend", 'ratings':[test_audience.pk]})
        self.assertTrue(self.form.is_valid())
        test_audience.delete()

    # Unit test for validation of empty howToProceed field - empty howToProceed field OK
    @tag('unit', 'forms')
    def test_trend_form_validation_for_empty_howToProceed_field(self):
        test_audience = AudienceMember(name='Student4')
        test_audience.save()
        self.form = TrendForm(data={'name': "Trend name", 'description': "Description of a trend", 'importance': "Importance of a trend", 'howToProceed': "", 'ratings':[test_audience.pk]})
        self.assertTrue(self.form.is_valid())
        test_audience.delete()

    # Unit test for validation of new non-empty field that's too long - field invalid, max length 50
    @tag('unit', 'forms')
    def test_trend_form_validation_for_field_over_max_length(self):
        self.form = TrendForm(data={'name': "The name field cannot be longer than 50 characters and this is longer than expected, far too long for the field."})
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new non-empty field under the max length - form valid
    @tag('unit', 'forms')
    def test_trend_form_validation_for_field_under_max_length(self):
        test_audience = AudienceMember(name='Student5')
        test_audience.save()
        self.form = TrendForm(data={'name': "Data in the Classroom", 'description': "Description about the trend.", 'importance': "Importance of the trend", 'howToProceed': "How to proceed from here.", 'ratings':[test_audience.pk]})
        self.assertTrue(self.form.is_valid())
        test_audience.delete()


# Unit tests for the ProjectForm
class TestProjectForm(TestCase):

    # Set up the form instance for the class
    @classmethod
    def setUp(cls):
        cls.form = ProjectForm()

    # Unit test existence of the description field in the Project Form
    @tag('unit', 'forms')
    def test_project_form_description_field(self):
        self.assertIn('name="description"', self.form.as_p())

    # Unit test existence of the principles field in the Project Form
    @tag('unit', 'forms')
    def test_project_form_principles_field(self):
        self.assertIn('id="id_principles"', self.form.as_p())

    # Unit test existence of the projects field in the Project Form
    @tag('unit', 'forms')
    def test_project_form_projects_field(self):
        self.assertIn('id="id_projects"', self.form.as_p())

    # Unit test existence of the short description field in the Project Form
    @tag('unit', 'forms')
    def test_project_form_short_description_field(self):
        self.assertIn('name="short_description"', self.form.as_p())

    # Unit test existence of the name field in the Project Form
    @tag('unit', 'forms')
    def test_project_form_name_field(self):
        self.assertIn('name="name"', self.form.as_p())

    # Unit test Project Form has fields to populate
    @tag('unit', 'forms')
    def test_project_form_has_seven_fields(self):
        self.assertEqual(7, len(self.form.fields))

    # Unit test for validation of empty form - empty form invalid
    @tag('unit', 'forms')
    def test_project_form_validation_for_no_input_provided(self):
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new empty name field - empty field invalid
    @tag('unit', 'forms')
    def test_project_form_validation_for_empty_field(self):
        self.form = ProjectForm(data={'name': ""})
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new non-empty field that's too long - field invalid, max length 50
    @tag('unit', 'forms')
    def test_project_form_validation_for_field_over_max_length(self):
        self.form = ProjectForm(data={'name': "The name field cannot be longer than 50 characters and this is longer than expected, far too long for the field."})
        self.assertFalse(self.form.is_valid())

    # Unit test for validation of new non-empty field under the max length - form valid
    @tag('unit', 'forms')
    def test_project_form_validation_for_field_under_max_length(self):
        self.form = ProjectForm(data={'description': "Longer description about the project ", 'principles': None, 'projects': None, 'short_description': "Short description about the project.", 'name': "Vizkit"})
        self.assertTrue(self.form.is_valid())