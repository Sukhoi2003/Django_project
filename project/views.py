from django.shortcuts import render
from django.http import HttpResponse


data = [
     {
    'id':'1',
    'title':'Econome web site',
    'description':'Economic firma web sayti'
},
{
    'id':'2',
    'title':'AliExpress',
    'description':'Katta kuryerlik kompaniyasi'
},
{
    'id':'3',
    'title':'Uzum',
    'description':'Uzbekistondagi savdo appi'
}
]

# Create your views here.
def projects(request):
    # return HttpResponse("Bu projects tomomnidan yozildi")
    return render(request, 'projects.html', {'data':data})


def project(request, pk):
    # return HttpResponse(f"Bu project tomomnidan yozildi --> {pk}")
    content = None
    for project in data:
        if project['id'] == str(pk):
            content = project
    return render(request, 'project.html', context=content)
