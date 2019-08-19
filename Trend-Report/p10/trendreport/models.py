import os
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import django
from django.utils import timezone
from taggit.managers import TaggableManager
from django.forms import CheckboxSelectMultiple, ModelChoiceField, ModelMultipleChoiceField, formset_factory
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseModel(models.Model):
    created_date = models.DateTimeField(default=django.utils.timezone.now, editable=False)
    modified_date = models.DateTimeField(default=django.utils.timezone.now, editable=False)

    class Meta:
        abstract = True


# BASE TABLES #
class AudienceMember(BaseModel):
    # Define Columns #
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=50, blank=True, default="user", help_text="Type the name of an icon from "
                                                                                        "http://fontawesome.io/icons/")

    # Set Manager #
    audience_member_manager = models.Manager()

    def __str__(self):
        return self.name


class Principle(BaseModel):
    # Define Columns #
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, default="lightbulb-o", help_text="Type the name of an icon from "
                                                                                        "http://fontawesome.io/icons/")

    # Set Manager #
    principle_manager = models.Manager()

    def __str__(self):
        return self.name


class Project(BaseModel):
    # Define Columns #
    name = models.CharField(max_length=50, unique=True)
    description = RichTextUploadingField(null=True)
    short_description = models.TextField(max_length=128, verbose_name='Short Description', blank=True,
                                         help_text="Short Description is used to let people know what the project "
                                                   "is about. If left blank, the first 128 "
                                                   "characters of the Description will be used")
    projects = models.ManyToManyField("self", blank=True, verbose_name="Related Projects")
    principles = models.ManyToManyField(Principle, blank=True, verbose_name="Related Principles")
    tags = TaggableManager(blank=True, help_text="Type tags separated by a comma")
    background = models.ImageField(default='default.jpg',
                                   blank=True,
                                   help_text="Recommended image ratio is 16:9")

    # Set Manager #
    project_manager = models.Manager()

    def __str__(self):
        return self.name


class Trend(BaseModel):
    # Define Columns #
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    short_description = models.TextField(max_length=128, verbose_name='Short Description', blank=True,
                                         help_text="Short Description is used to let people know what the trend "
                                                   "is about. If left blank, the first 128 "
                                                   "characters of the Description will be used")
    importance = models.TextField(null=True, blank=True)
    howToProceed = models.TextField(null=True, verbose_name='How to Proceed', blank=True)
    examples = models.TextField(null=True, blank=True)
    projects = models.ManyToManyField(Project, blank=True, help_text="Select related projects",
                                      verbose_name="Related Projects")
    principles = models.ManyToManyField(Principle, blank=True, help_text="Select related principles",
                                        verbose_name="Related Principles")
    ratings = models.ManyToManyField(AudienceMember, through='Score')
    tags = TaggableManager(blank=True, help_text="Type tags separated by a comma")
    background = models.ImageField(default='default.jpg',
                                   blank=True,
                                   help_text="Recommended image ratio is 16:9")

    # Set Manager #
    trend_manager = models.Manager()

    def __str__(self):
        return self.name


class Score(models.Model):
    CHOICES = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]
    trend = models.ForeignKey(Trend, on_delete=models.CASCADE)
    audienceMember = models.ForeignKey(AudienceMember, on_delete=models.CASCADE, help_text="Select audience member")
    score = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)],
                                     choices=CHOICES, help_text="Select score")

    # Set Manager #
    scores_manager = models.Manager()

    def __str__(self):
        return "Audience Member"


class Admin(models.Model):
    name = models.CharField(max_length=64, default="ICT Techlab",
                            help_text="Set the title for the ICT Techlab About page")
    tagline = models.TextField(blank=True, help_text="This will appear in a big font under the title.")
    description = models.TextField()
    image = models.ImageField(default='background_images/trend.jpg', blank=True,
                              help_text="Set a background for the page. "
                                        "Recommended image ratio is 16:9")

    # Set Manager #
    admin_manager = models.Manager()

    def __str__(self):
        return "Main Admin"


