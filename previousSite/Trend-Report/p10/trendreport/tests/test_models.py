from django.test import TestCase
import unittest
from django.core.urlresolvers import reverse
from django.urls import resolve
from trendreport.models import Admin, Score, Trend, Project, Principle, AudienceMember, BaseModel

from unittest import TestCase
from mock import MagicMock
from mock_django.models import ModelMock
import datetime
from datetime import timedelta
from django.utils import timezone
from django.test import tag

### MODELS UNIT TESTS ###

# Unit testing the models with mock objects to segregate testing from ORM database coupling
# These tests are intended to use static data only and do not engage with the (test) database for the model being tested
# To run tests:
#    For all tests: 'py manage.py test trendreport'
#    To filter tests by their tags (say you want to run just the unit tests): 'py manage.py test trendreport --tag=unit'
#    NB: Tags for tests can be found above the test function eg @tag('unit')


# Unit tests for the Base Model
class TestBaseModel(TestCase):

    # Set up the mock base model for the whole class with values
    @classmethod
    def setUp(cls):
        cls.mock_base = MagicMock(BaseModel)
        cls.mock_base.created_date = cls.created_date = timezone.now()
        cls.mock_base.modified_date = cls.modified_date = timezone.now()

    # Unit test for the base model created date
    @tag('unit', 'models')
    def test_base_model_created_date(self):
        self.assertEquals(self.mock_base.created_date, self.created_date)

    # Unit test for the base model modified date
    @tag('unit', 'models')
    def test_base_model_modified_date(self):
        self.assertEquals(self.mock_base.modified_date, self.modified_date)

    # Unit test to check created and modified dates are the same
    @tag('unit', 'models')
    def test_base_model_dates_are_the_same(self):
        self.assertEquals(self.mock_base.created_date, self.mock_base.modified_date)

    # Unit test for base model to check dates are different after one has been changed
    @tag('unit', 'models')
    def test_base_model_dates_are_different_after_modification(self):
        self.mock_base.modified_date = timezone.now() + timedelta(days=1)
        self.assertNotEquals(self.mock_base.created_date, self.mock_base.modified_date)


# Unit tests for the AudienceMember model
class TestAudienceMemberModel(TestCase):

    # Set up the mock audience model for the whole class with values
    @classmethod
    def setUp(cls):
        cls.mock_audience = MagicMock(AudienceMember)
        cls.mock_audience.name = 'Student'

    # Unit test the audience name
    @tag('unit', 'models')
    def test_audience_model_name(self):
        self.assertEquals(self.mock_audience.name, 'Student')

    # Unit test an audience name change still returns correct value
    @tag('unit', 'models')
    def test_audience_model_name_update(self):
        self.mock_audience.name = 'Graduate'
        self.assertEquals(self.mock_audience.name, 'Graduate')
        self.assertNotEquals(self.mock_audience.name, 'Student')


# Unit tests for the Principle model
class TestPrincipleModel(TestCase):

    # Set up the mock principle model for the whole class with values
    @classmethod
    def setUp(cls):
        cls.mock_principle = MagicMock(Principle)
        cls.mock_principle.name = 'Mobile first'
        cls.mock_principle.description = 'We extend the University experience to the devices people use daily, on and off campus.'
        cls.mock_principle.icon = 'fa-tablet'

    # Unit test the principle name
    @tag('unit', 'models')
    def test_principle_model_name(self):
        self.assertEquals(self.mock_principle.name, 'Mobile first')

    # Unit test a principle name change
    @tag('unit', 'models')
    def test_principle_model_name_change(self):
        self.mock_principle.name = 'Commoditised'
        self.assertEquals(self.mock_principle.name, 'Commoditised')
        self.assertNotEquals(self.mock_principle.name, 'Mobile first')

    # Unit test the principle description
    @tag('unit', 'models')
    def test_principle_model_description(self):
        self.assertEquals(self.mock_principle.description, 'We extend the University experience to the devices people use daily, on and off campus.')

    # Unit test the principle description change
    @tag('unit', 'models')
    def test_principle_model_description_change(self):
        self.mock_principle.description = 'We standardise elements and processes where applicable, freeing our colleagues to focus on adding value to our core strategic direction.'
        self.assertEquals(self.mock_principle.description, 'We standardise elements and processes where applicable, freeing our colleagues to focus on adding value to our core strategic direction.')
        self.assertNotEquals(self.mock_principle.description, 'We extend the University experience to the devices people use daily, on and off campus.')

    # Unit test the principle icon
    @tag('unit', 'models')
    def test_principle_model_icon(self):
        self.assertEquals(self.mock_principle.icon, 'fa-tablet')

    #Unit test a principle icon change
    @tag('unit', 'models')
    def test_principle_icon_change(self):
        self.mock_principle.icon = 'fa-bars'
        self.assertEquals(self.mock_principle.icon, 'fa-bars')
        self.assertNotEquals(self.mock_principle.icon, 'fa-tablet')


# Unit tests for the Project model
class TestProjectModel(TestCase):

    # Set up the mock principle model for the whole class with values
    @classmethod
    def setUp(cls):
        cls.mock_project = MagicMock(Project)
        cls.mock_project.name = 'The Digital Strategy'
        cls.mock_project.description = 'What is the most effective way to share the Digital Experience to the greater community and amongst our peers.'
        cls.mock_project.short_description = 'What is the most effective way to share the Digital Experience...'

    # Unit test the project name
    @tag('unit', 'models')
    def test_project_model_name(self):
        self.assertEquals(self.mock_project.name, 'The Digital Strategy')

    # Unit test a project name change
    @tag('unit', 'models')
    def test_project_model_name_change(self):
        self.mock_project.name = 'SFIA'
        self.assertEquals(self.mock_project.name, 'SFIA')
        self.assertNotEquals(self.mock_project.name, 'The Digital Strategy')

    # Unit test the project description
    @tag('unit', 'models')
    def test_project_model_description(self):
        self.assertEquals(self.mock_project.description, 'What is the most effective way to share the Digital Experience to the greater community and amongst our peers.')

    # Unit test a project description change
    @tag('unit', 'models')
    def test_project_model_description_change(self):
        self.mock_project.description = 'An app to help staff measure and improve their Skills for the Information Age. Based on the Framework of the same name.'
        self.assertEquals(self.mock_project.description, 'An app to help staff measure and improve their Skills for the Information Age. Based on the Framework of the same name.')
        self.assertNotEquals(self.mock_project.name, 'What is the most effective way to share the Digital Experience to the greater community and amongst our peers.')

    # Unit test the project short description
    @tag('unit', 'models')
    def test_project_model_short_description(self):
        self.assertEquals(self.mock_project.short_description, 'What is the most effective way to share the Digital Experience...')

    # Unit test a project short description change
    @tag('unit', 'models')
    def test_project_model_short_description_change(self):
        self.mock_project.description = 'An app to help staff measure and improve their Skills for the Information Age...'
        self.assertEquals(self.mock_project.description, 'An app to help staff measure and improve their Skills for the Information Age...')
        self.assertNotEquals(self.mock_project.name, 'What is the most effective way to share the Digital Experience...')


# Unit tests for the Trend model
class TestTrendModel(TestCase):

    # Set up the mock principle model for the whole class with values
    @classmethod
    def setUp(cls):
        cls.mock_trend = MagicMock(Trend)
        cls.mock_trend.name = 'Data in the Classroom'
        cls.mock_trend.description = 'Using big data and data analytics, researchers can visualise complex concepts as interactive graphs, charts and maps. This can serve as dynamic yet accessible learning collateral for students to use in and outside the classroom. By unifying large amounts of data, the students can also discern new relationships and reach new conclusions.'
        cls.mock_trend.short_description = 'Using big data and data analytics, researchers can visualise complex concepts as interactive graphs, charts and maps. This can s'
        cls.mock_trend.importance = 'Academics are seeking new ways of engaging students while sharing knowledge, recognising the need for science communication. Data science in the classroom is one of the key tools that can enable this, and there are currently several activities at the University to support this emerging requirement, and data science is making its way into diverse curriculum.'
        cls.mock_trend.howToProceed = 'By providing rapidly evolving toolsets for data visualisation and data science, we can help faculties and students that lack the capability for data science. We should also nurture multidisciplinary approaches to the challenges faced by our students in understanding and communicating science.'
        cls.mock_trend.examples = 'Vizkit, Dataviz Course SiT, supporting Hadoop clusters, Phil\'s Datascience Course.'

    # Unit test the trend name
    @tag('unit', 'models')
    def test_trend_model_name(self):
        self.assertEquals(self.mock_trend.name, 'Data in the Classroom')

    # Unit test a trend name change
    @tag('unit', 'models')
    def test_trend_model_name_changed(self):
        self.mock_trend.name = 'Affective Computing'
        self.assertEquals(self.mock_trend.name, 'Affective Computing')
        self.assertNotEquals(self.mock_trend.name, 'Data in the Classroom')

    # Unit test the trend description
    @tag('unit', 'models')
    def test_trend_model_description(self):
        self.assertEquals(self.mock_trend.description, 'Using big data and data analytics, researchers can visualise complex concepts as interactive graphs, charts and maps. This can serve as dynamic yet accessible learning collateral for students to use in and outside the classroom. By unifying large amounts of data, the students can also discern new relationships and reach new conclusions.')

    # Unit test a trend description change
    @tag('unit', 'models')
    def test_trend_model_description_change(self):
        self.mock_trend.description = 'New systems and devices will help us recognise, interpret, process and simulate human affects. This will enable us to sense the emotional state of users by measuring changes in heart rate and galvanic skin response, body temperature, posture and gestures, verbal content, the rhythm of their keystrokes and facial expressions.'
        self.assertEquals(self.mock_trend.description, 'New systems and devices will help us recognise, interpret, process and simulate human affects. This will enable us to sense the emotional state of users by measuring changes in heart rate and galvanic skin response, body temperature, posture and gestures, verbal content, the rhythm of their keystrokes and facial expressions.')
        self.assertNotEquals(self.mock_trend.description, 'Using big data and data analytics, researchers can visualise complex concepts as interactive graphs, charts and maps. This can serve as dynamic yet accessible learning collateral for students to use in and outside the classroom. By unifying large amounts of data, the students can also discern new relationships and reach new conclusions.')

    # Unit test the trend short description
    @tag('unit', 'models')
    def test_trend_model_short_description(self):
        self.assertEquals(self.mock_trend.short_description, 'Using big data and data analytics, researchers can visualise complex concepts as interactive graphs, charts and maps. This can s')

    # Unit test a trend short description change
    @tag('unit', 'models')
    def test_trend_model_short_description_change(self):
        self.mock_trend.short_description = 'New systems and devices will help us recognise, interpret, process and simulate human affects. This will enable us to sense the'
        self.assertEquals(self.mock_trend.short_description, 'New systems and devices will help us recognise, interpret, process and simulate human affects. This will enable us to sense the')
        self.assertNotEquals(self.mock_trend.short_description, 'Using big data and data analytics, researchers can visualise complex concepts as interactive graphs, charts and maps. This can s')

    # Unit test the trend importance
    @tag('unit', 'models')
    def test_trend_model_importance(self):
        self.assertEquals(self.mock_trend.importance, 'Academics are seeking new ways of engaging students while sharing knowledge, recognising the need for science communication. Data science in the classroom is one of the key tools that can enable this, and there are currently several activities at the University to support this emerging requirement, and data science is making its way into diverse curriculum.')

    # Unit test a trend importance change
    @tag('unit', 'models')
    def test_trend_model_importance_change(self):
        self.mock_trend.importance = 'Affective computing can be invaluable for tailoring the presentation style of a computerised tutor to the learner, whether they are disengaged, interested, frustrated or amused. In particular, there is interest among educators in the area of distance education, with the goal being able to determine what will keep remote students engaged.'
        self.assertEquals(self.mock_trend.importance, 'Affective computing can be invaluable for tailoring the presentation style of a computerised tutor to the learner, whether they are disengaged, interested, frustrated or amused. In particular, there is interest among educators in the area of distance education, with the goal being able to determine what will keep remote students engaged.')
        self.assertNotEquals(self.mock_trend.importance, 'Academics are seeking new ways of engaging students while sharing knowledge, recognising the need for science communication. Data science in the classroom is one of the key tools that can enable this, and there are currently several activities at the University to support this emerging requirement, and data science is making its way into diverse curriculum.')

    # Unit test the trend "howToProceed"
    @tag('unit', 'models')
    def test_trend_model_how_to_proceed(self):
        self.assertEquals(self.mock_trend.howToProceed, 'By providing rapidly evolving toolsets for data visualisation and data science, we can help faculties and students that lack the capability for data science. We should also nurture multidisciplinary approaches to the challenges faced by our students in understanding and communicating science.')

    # Unit test a trend "howToProceed" change
    @tag('unit', 'models')
    def test_trend_model_how_to_proceed_change(self):
        self.mock_trend.howToProceed = 'This emerging technology is appearing in small scale projects at the University. New partnerships and continued research in affective computing will help develop online computer-based learning environments to a degree where they can respond seamlessly to a learner\'s needs.'
        self.assertEquals(self.mock_trend.howToProceed, 'This emerging technology is appearing in small scale projects at the University. New partnerships and continued research in affective computing will help develop online computer-based learning environments to a degree where they can respond seamlessly to a learner\'s needs.')
        self.assertNotEquals(self.mock_trend.howToProceed, 'By providing rapidly evolving toolsets for data visualisation and data science, we can help faculties and students that lack the capability for data science. We should also nurture multidisciplinary approaches to the challenges faced by our students in understanding and communicating science.')

    # Unit test the trend examples
    @tag('unit', 'models')
    def test_trend_model_examples(self):
        self.assertEquals(self.mock_trend.examples, 'Vizkit, Dataviz Course SiT, supporting Hadoop clusters, Phil\'s Datascience Course.')

    # Unit test a trend examples change
    @tag('unit', 'models')
    def test_trend_model_examples_change(self):
        self.mock_trend.examples =  'Brain Computer Interface, MIDEA course, Central park, Neuropharma, Ontask'
        self.assertEquals(self.mock_trend.examples, 'Brain Computer Interface, MIDEA course, Central park, Neuropharma, Ontask')
        self.assertNotEquals(self.mock_trend.examples, 'Vizkit, Dataviz Course SiT, supporting Hadoop clusters, Phil\'s Datascience Course.')


# Unit tests for the Score model
class TestScoreModel(TestCase):

    # Set up the mock base model for the whole class with values
    @classmethod
    def setUp(cls):
        cls.mock_score = MagicMock(Score)
        cls.mock_score.score = 5

    # Unit test for getting score value
    @tag('unit', 'models')
    def test_score_value(self):
        self.assertEquals(self.mock_score.score, 5)

    # Unit test a score value change
    @tag('unit', 'models')
    def test_score_value_change(self):
        self.mock_score.score = 7
        self.assertEquals(self.mock_score.score, 7)
        self.assertNotEquals(self.mock_score.score, 5)


# Unit tests for the Admin model
class TestAdminModel(TestCase):

    # Set up the mock base model for the whole class with values
    @classmethod
    def setUp(cls):
        cls.mock_admin = MagicMock(Admin)
        cls.mock_admin.name = 'The ICT Techlab'
        cls.mock_admin.description = 'Trends continue to emerge both in and outside the education sector. ICT is committed to addressing and leveraging these trends to support the University strategy. The increased collaboration and accelerating rates of disruption introduce challenges and opportunities to the University\'s core strategies of research and education. In this website, we examine some of the latest trends of significance to the University, outlining their impact and providing suggestions on how to best proceed with them. It is designed to help us understand the horizon of trends from each field?s perspective. The trends listed here are not linear in nature, and their concepts will continually change. Some trends are imminent and should be addressed immediately, while others are emerging and may not impact the University for some time. Where a decision to proceed is made for any listed trend, our suggestions outline some potential activities we can undertake within the innovation framework. As we and other organisations experiment within these trends, new opportunities may arise and these suggestions may change to reflect this.'

    # Unit test the admin name
    @tag('unit', 'models')
    def test_admin_model_name(self):
        self.assertEquals(self.mock_admin.name, 'The ICT Techlab')

    # Unit test a admin name change
    @tag('unit', 'models')
    def test_admin_model_name_change(self):
        self.mock_admin.name = 'ICT Techlab'
        self.assertEquals(self.mock_admin.name, 'ICT Techlab')
        self.assertNotEquals(self.mock_admin.name, 'The ICT Techlab')

    # Unit test the admin description
    @tag('unit', 'models')
    def test_admin_model_description(self):
        self.assertEquals(self.mock_admin.description, 'Trends continue to emerge both in and outside the education sector. ICT is committed to addressing and leveraging these trends to support the University strategy. The increased collaboration and accelerating rates of disruption introduce challenges and opportunities to the University\'s core strategies of research and education. In this website, we examine some of the latest trends of significance to the University, outlining their impact and providing suggestions on how to best proceed with them. It is designed to help us understand the horizon of trends from each field?s perspective. The trends listed here are not linear in nature, and their concepts will continually change. Some trends are imminent and should be addressed immediately, while others are emerging and may not impact the University for some time. Where a decision to proceed is made for any listed trend, our suggestions outline some potential activities we can undertake within the innovation framework. As we and other organisations experiment within these trends, new opportunities may arise and these suggestions may change to reflect this.')

    # Unit test a admin description change
    @tag('unit', 'models')
    def test_admin_model_description_change(self):
        self.mock_admin.description = 'Trends continue to emerge both in and outside the education sector. ICT is committed to addressing and leveraging these trends to support the University strategy. The increased collaboration and accelerating rates of disruption introduce challenges and opportunities to the University\'s core strategies of research and education. In this website, we examine some of the latest trends of significance to the University, outlining their impact and providing suggestions on how to best proceed with them. It is designed to help us understand the horizon of trends from each field?s perspective. The trends listed here are not linear in nature, and their concepts will continually change.'
        self.assertEquals(self.mock_admin.description, 'Trends continue to emerge both in and outside the education sector. ICT is committed to addressing and leveraging these trends to support the University strategy. The increased collaboration and accelerating rates of disruption introduce challenges and opportunities to the University\'s core strategies of research and education. In this website, we examine some of the latest trends of significance to the University, outlining their impact and providing suggestions on how to best proceed with them. It is designed to help us understand the horizon of trends from each field?s perspective. The trends listed here are not linear in nature, and their concepts will continually change.')
        self.assertNotEquals(self.mock_admin.description, 'Trends continue to emerge both in and outside the education sector. ICT is committed to addressing and leveraging these trends to support the University strategy. The increased collaboration and accelerating rates of disruption introduce challenges and opportunities to the University\'s core strategies of research and education. In this website, we examine some of the latest trends of significance to the University, outlining their impact and providing suggestions on how to best proceed with them. It is designed to help us understand the horizon of trends from each field?s perspective. The trends listed here are not linear in nature, and their concepts will continually change. Some trends are imminent and should be addressed immediately, while others are emerging and may not impact the University for some time. Where a decision to proceed is made for any listed trend, our suggestions outline some potential activities we can undertake within the innovation framework. As we and other organisations experiment within these trends, new opportunities may arise and these suggestions may change to reflect this.')