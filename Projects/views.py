from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm

# List View
def project_list_view(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

# Detail View
def project_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

@login_required
def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'project_form.html', {'form': form})

# Update View
@login_required
def project_update_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'project_form.html', {'form': form})

# Delete View
@login_required
def project_delete_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'project_confirm_delete.html', {'project': project})