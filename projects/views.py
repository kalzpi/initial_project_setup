from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from . import models as project_models
from rolls import models as roll_models


def ProjectDetailView(request, pk):
    try:
        project = project_models.Project.objects.get(pk=pk)
        return render(request, "projects/detail.html", {"project": project})
    except project_models.Project.DoesNotExist:
        raise Http404()


class ProjectListView(ListView):
    model = project_models.Project
    template_name = "projects/list.html"
    paginate_by = 5
    ordering = "created"
