from django import forms
from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple, inlineformset_factory
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AudienceMemberForm(forms.ModelForm):

    class Meta:
        exclude = ()
        model = AudienceMember
        widgets = {
            'name': forms.Textarea(attrs={
                'rows': 1,
                'maxlength': '50',
            })
        }


class PrincipleForm(forms.ModelForm):

    class Meta:
        exclude = ()
        model = Principle
        widgets = {
            'name': forms.Textarea(attrs={
                'rows': 1,
                'maxlength': '50',
            })
        }


class TrendForm(forms.ModelForm):

    class Meta:
        exclude = ()
        model = Trend
        widgets = {
            'principles': CheckboxSelectMultiple,
            'projects': CheckboxSelectMultiple,
            'short_description': forms.Textarea(attrs={
                'rows': 5,
                'maxlength': '128',
            }),
            'name': forms.Textarea(attrs={
                'rows': 1,
                'maxlength': '50',
            })
        }


class ProjectForm(forms.ModelForm):

    class Meta:
        exclude = ()
        model = Project
        widgets = {
            'description': CKEditorUploadingWidget,
            'principles': CheckboxSelectMultiple,
            'projects': CheckboxSelectMultiple,
            'short_description': forms.Textarea(attrs={
                'rows': 5,
                'maxlength': '128',
            }),
            'name': forms.Textarea(attrs={
                'rows': 1,
                'maxlength': '50',
            })
        }
