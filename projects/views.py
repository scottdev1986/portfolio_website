from django.shortcuts import render, get_object_or_404

from projects.models import Project

def projects(request, slug):
    projects = get_object_or_404(Project,slug=slug)

    context = {
        'projects' : projects
    }

    return render(request, 'projects/project_details.html', context)
