
from django.shortcuts import render
from projects.models import Project

def project_index(request):
    ''' for listing projects.'''
    projects = Project.objects.all()
    context = {
      'projects':  projects 
    }
    return render(request,'project_index.html', context)

def project_detail(request,pk):
    '''
    to detail page of project.
    '''
    project=Project.objects.get(pk=pk)
    context ={ 
        'project':project
    }
    return render(request,'project_detail.html',context)
    