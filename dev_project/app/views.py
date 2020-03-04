from django.shortcuts import render
from .forms import UploadFileForm, FindUser
from .csv_parser import csv_parser
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import User
from errors import errors


def main_page(request):
    return render(request, 'main_page.html')


def find_person(request):
    if request.method == 'POST':
        form = FindUser(request.POST)
        if form.is_valid():
            person = form.cleaned_data['person'].split(" ")
            try:
                users = User.objects.filter(name__iexact=person[0], surname__iexact=person[1])
            except:
                users = User.objects.filter(name__iexact=person[0])
                if len(users) == 0:
                    users = User.objects.filter(surname__iexact=person[0])
            return render(request, 'find_person.html', {'form': form, 'users': users})
    else:
        form = FindUser()
    return render(request, 'find_person.html', {'form': form, 'users': []})


def import_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith(".csv"):
                messages.error(request, 'Вы загрузили не csv файл')
                return HttpResponseRedirect(reverse('import_data'))
            else:
                error = csv_parser(csv_file)
                if error:
                    messages.error(request, str(list(errors.keys())[list(errors.values()).index(error)]))
                    return HttpResponseRedirect('/import_data')
                else:
                    return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'import_data.html', {'form': form})
