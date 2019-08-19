from django.contrib import admin
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# Define Classes
class ScoreInline(admin.TabularInline):
    model = Score
    extra = 1


class AudienceMemberFormAdmin(admin.ModelAdmin):
    form = AudienceMemberForm


class PrincipleFormAdmin(admin.ModelAdmin):
    form = PrincipleForm


class TrendFormAdmin(admin.ModelAdmin):
    form = TrendForm
    inlines = [ScoreInline]


class ProjectFormAdmin(admin.ModelAdmin):
    form = ProjectForm

# Register classes in admin
admin.site.register(Trend, TrendFormAdmin)
admin.site.register(Project, ProjectFormAdmin)
admin.site.register(Principle, PrincipleFormAdmin)
admin.site.register(AudienceMember, AudienceMemberFormAdmin)
admin.site.register(Admin)

