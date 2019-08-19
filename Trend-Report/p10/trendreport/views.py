# -*- coding: utf-8 -*-
import json

# Forms
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .forms import *
from .models import Trend

from django.db.models import Q

def trends_index(request):

    # Data to send to the template
    context = {
        'selected_audience': request.GET.get('audience', ''),
        'audience_members': [],
        'audience_scores': {},
        'trends': []
    }

    # Get the audience members for the filter
    audience = AudienceMember.audience_member_manager.all()
    for a in audience:
        context['audience_members'].append({
            'id': a.id,
            'icon': a.icon,
            'name': a.name
        })

    # Query the database for trends
    trends = Trend.trend_manager.order_by('-modified_date')
    for t in trends:

        trend_data = {
            'id': t.id,
            'name': t.name,
            'description': t.description,
            'short_description': t.short_description,
            'background': "images/" + str(t.background),
        }

        # Index audience scores by trend id
        for am in t.score_set.all():

            if t.id not in context['audience_scores']:
                context['audience_scores'][t.id] = {}

            if am.audienceMember_id not in context['audience_scores'][t.id]:
                context['audience_scores'][t.id][am.audienceMember_id] = 0

            context['audience_scores'][t.id][am.audienceMember_id] = am.score

        context['trends'].append(trend_data)

    # Send the data, render the template
    return render(request, 'trendreport/trend-list.html', context)


def trend_page(request, trend_id):

    # Query the database
    trend = Trend.trend_manager.get(id=trend_id)

    # Data to send to the template
    context = {
        'trend': {
            'id': trend.id,
            'name': trend.name,
            'description': trend.description,
            'importance': trend.importance,
            'proceed': trend.howToProceed,
            'projects': [],
            'principles': [],
            'tags': [],
            'background': "images/" + str(trend.background),
            'short_description' : trend.short_description,
        }
    }

    # Get the trend's related projects
    for p in trend.projects.all():
        context['trend']['projects'].append({
            'id': p.id,
            'name': p.name,
            'short_description': p.short_description,
            'background': "images/" + str(p.background),
        })

    # Get the trend's related principles
    for p in trend.principles.all():
        context['trend']['principles'].append({
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'icon': p.icon
        })

    # Get the trend's related tags
    for t in trend.tags.all():
        context['trend']['tags'].append({
            'id': t.id,
            'name': t.name,
            # todo: do we need a slug? for linking or whatever
        })

    # Send the data, render the template
    return render(request, 'trendreport/trend.html', context)


def project_page(request, project_id):

    # Query the database
    project = Project.project_manager.get(id=project_id)

    # Get the project data
    context = {
        'project': {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'background': "images/" + str(project.background),
            'trends': [],
            'projects': [],
            'principles': [],
            'tags': [],
            'short_description': project.short_description,
        }
    }

    # Get the projects's related trends
    for t in project.trend_set.all():
        context['project']['trends'].append({
            'id': t.id,
            'name': t.name,
            'short_description': t.short_description,
            'background': "images/" + str(t.background)
        })

    # Get the projects's related projects
    for p in project.projects.all():
        context['project']['projects'].append({
            'id': p.id,
            'name': p.name,
            'short_description': p.short_description,
            'background': "images/" + str(p.background),
        })

    # Get the projects's related principles
    for p in project.principles.all():
        context['project']['principles'].append({
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'icon': p.icon
        })

    # Get the projects's related tags
    for t in project.tags.all():
        context['project']['tags'].append({
            'id': t.id,
            'name': t.name,
            # todo: do we need a slug? for linking or whatever
        })

    # Send the data, render the template
    return render(request, 'trendreport/project.html', context)


def principles_page(request):

    # Query the database
    principles = Principle.principle_manager.all()

    # Setup context variable
    context = {
        'principles': []
    }

    # Data to send to the template
    for principle in principles:
        context['principles'].append({
            'id': principle.id,
            'icon': "fa-" + principle.icon,
            'name': principle.name,
            'description': principle.description
        })

    # Send the data, render the template
    return render(request, 'trendreport/principles.html', context)


def icttechlab_page(request):

    # Query the database
    admin = Admin.admin_manager.get()

    # Data to send to the template
    context = {
        'admin': {
            'name': admin.name,
            'tagline': admin.tagline,
            'description': admin.description,
            'background': "images/" + str(admin.image),
        }
    }

    return render(request, 'trendreport/ict-techlab.html', context)


def search_page(request, query):

    context = {
        'trend_results': '[]',
        'project_results': '[]'
    }

    search_query = request.GET.get('q', '');

    if search_query:

        trend_result = Trend.trend_manager.filter(Q(name__icontains=search_query)
                            | Q(description__icontains=search_query)
                            | Q(importance__icontains=search_query)
                            | Q(howToProceed__icontains=search_query)
                            | Q(examples__icontains=search_query)
                            | Q(tags__name__icontains=search_query)).distinct().order_by('name')

        project_result = Project.project_manager.filter(Q(name__icontains=search_query)
                            | Q(description__icontains=search_query)
                            | Q(tags__name__icontains=search_query)).distinct().order_by('name')

        context = {
            'trend_results': serializers.serialize('json', trend_result),
            'project_results': serializers.serialize('json', project_result),
        }

    return HttpResponse(json.dumps(context), content_type='application/json')


handler404 = 'mysite.views.my_custom_page_not_found_view'

def custom_404_page(request):
    return render(request, 'trendreport/custom_404.html')

def custom_500_page(request):
    return render(request, 'trendreport/custom_500.html')
