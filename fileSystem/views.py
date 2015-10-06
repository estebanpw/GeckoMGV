from django.shortcuts import render
from fileSystem.forms import *
from fileSystem.models import *
from django.http import HttpResponse
from MGV.views import *
import csv

# Create your views here.

def generate_SavePath(request, filename):
    url = "media/files/users/%s/%s" % (request.user.username, filename)
    return url

def uploadFile(request):
    print "UploadingFile..."
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            newFile = userFile(user=request.user, file=request.FILES['userfile'])
            newFile.save()
    return userFile.objects.filter(user = request.user)

def createFile(request, content, filename):
    print "Creating file..."
    path = generate_SavePath(request, filename)
    file = open(path,'wb')
    file.write(content)
    file.close()
    newFile = userFile(user=request.user, file=path)
    newFile.save()
    return userFile.objects.get(file=path)

def deleteFile(request):
    print "Deleting File..."
    if request.method == 'POST':
        form = DeleteFileForm(request.POST)
        if form.is_valid():
            userFile.objects.get(file=request.POST.get('filename')).delete()
            os.remove(request.POST.get('filename'))
    return userFile.objects.filter(user=request.user)

def fileManager_view(request):
    form = FileForm()
    if request.user.is_authenticated():
        files = userFile.objects.filter(user = request.user)
        return render(request, 'filemanager.html', {'form': form, 'files': files})
    else:
        return render(request, 'filemanager.html', {'form': form, 'files': {} })

def uploadFile_view(request):
    form = FileForm()
    files = uploadFile(request)
    return render(request, 'filemanager.html', {'form': form, 'files': files})

def deleteFile_view(request):
    form = FileForm()
    files = deleteFile(request)
    return render(request, 'filemanager.html', {'form': form, 'files': files})

def fileViewer_view(request):
    if request.user.is_authenticated():
        file = open(str(userFile.objects.get(file = request.POST.get('filename')).file), 'r')
        content = file.read()
        print content
        file.close()
        return render(request, 'fileViewer.html', {'fileName': request.POST.get('filename'), 'content': content})

def listUserFiles(request):
    if request.user.is_authenticated():
        files = userFile.objects.filter(user=request.user)
        return files