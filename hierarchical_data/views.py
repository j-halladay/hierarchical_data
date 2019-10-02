from django.shortcuts import render
from hierarchical_data.models import File_Class
# from ghost_post.forms import AddMessage
from django.http import HttpResponseRedirect
from django.urls import reverse
from hierarchical_data.forms import LoginForm, AddFile, AddFolder
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


@login_required
def homepage(request, *args, **kwargs):
    html = 'homepage.html'
    return render(request, html, {'files': File_Class.objects.all().filter(owner=request.user)})


def addfile(request, id, *args, **kwargs):
    html = 'genericform.html'
    if request.method == "POST":
        form = AddFile(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File_Class.objects.create(name=data['name'], parent=File_Class.objects.get(id=id), is_folder=False, file_link=data['file_link'], owner=request.user

                                      )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddFile()

    return render(request, html, {'form': form})


def addfolder(request, id, *args, **kwargs):
    html = 'genericform.html'
    if request.method == "POST":
        form = AddFolder(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File_Class.objects.create(name=data['name'], parent=File_Class.objects.get(id=id), is_folder=True, owner=request.user

                                      )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddFolder()

    return render(request, html, {'form': form})


class LoginPage(TemplateView):
    html = 'genericform.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()

        return render(request, self.html, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = authenticate(
                username=data['username'], password=data['password'])
            if u is not None:
                login(request, u)
            else:
                return HttpResponseRedirect(reverse('login'))
            destination = request.GET.get('next')
            if destination is not None:
                return HttpResponseRedirect(destination)
            else:
                return HttpResponseRedirect(reverse('homepage'))


class LogoutPage(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(reverse('homepage'))
