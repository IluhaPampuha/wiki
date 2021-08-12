from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Company, Messages
from .forms import CompanyForm, IncomingForm, OutgoingForm


# Create your views here.

def wiki(request):
    company = Company.objects.all()
    if request.method == "GET":
        return render(request, 'wiki_app/home.html', {"company": company, "form": CompanyForm()})
    else:
        try:
            form = CompanyForm(request.POST)
            newcompany = form.save(commit=False)
            newcompany.user = request.user
            newcompany.save()
            return redirect("/")
        except ValueError:
            return render(request, 'wiki_app/home.html',
                          {"company": company, "form": CompanyForm(),
                           "error": "Для добавления организации необходимо авторизоваться"})


def detail(request, id):
    messages = Messages.objects.filter(id_company=id)
    company = get_object_or_404(Company, pk=id)
    return render(request, "wiki_app/detail.html", {"company": company, "messages": messages})


def message(request, id_message):
    messages = get_object_or_404(Messages, pk=id_message)
    id = messages.id_company
    if messages.incoming_number == "":
        form = OutgoingForm(instance=messages)
    else:
        form = IncomingForm(instance=messages)
    if request.method == "GET":
        return render(request, "wiki_app/message.html", {"messages": messages, "form": form})
    else:
        try:
            if messages.incoming_number == "":
                form = OutgoingForm(request.POST, instance=messages)
                newoutgoing = form.save(commit=False)
                newoutgoing.user = request.user
                newoutgoing.save()
                return redirect(f"/company{id}/")
            else:
                form = IncomingForm(request.POST, instance=messages)
                newincoming = form.save(commit=False)
                newincoming.user = request.user
                newincoming.save()
                return redirect(f"/company{id}/")
        except ValueError:
            return render(request, "wiki_app/message.html", {"messages": messages, "form": form,
                                                             "error": "Для редактирования письма необходимо авторизоваться"})


def incoming(request, id):
    messages = Messages.objects.filter(id_company=id)
    company = get_object_or_404(Company, pk=id)
    if request.method == "GET":
        return render(request, "wiki_app/incoming.html",
                      {"company": company, "messages": messages, "form": IncomingForm()})
    else:
        try:
            form = IncomingForm(request.POST)
            if form.is_valid():
                newincoming = form.save(commit=False)
                newincoming.user = request.user
                newincoming.save()
                return redirect(f"/company{id}/")
        except ValueError:
            return render(request, "wiki_app/incoming.html",
                          {"company": company, "messages": messages, "form": IncomingForm(),
                           "error": "Для добавления организации необходимо авторизоваться"})


def outgoing(request, id):
    messages = Messages.objects.filter(id_company=id)
    company = get_object_or_404(Company, pk=id)
    if request.method == "GET":
        return render(request, "wiki_app/outgoing.html",
                      {"company": company, "messages": messages, "form": OutgoingForm()})
    else:
        try:
            form = OutgoingForm(request.POST)
            if form.is_valid():
                newoutgoing = form.save(commit=False)
                newoutgoing.user = request.user
                newoutgoing.save()
                return redirect(f"/company{id}/")
        except ValueError:
            return render(request, "wiki_app/outgoing.html",
                          {"company": company, "messages": messages, "form": OutgoingForm(),
                           "error": "Для добавления организации необходимо авторизоваться"})


def signupuser(request):
    if request.method == "GET":
        return render(request, 'wiki_app/signupuser.html', {"form": UserCreationForm()})
    else:
        # Создание нового пользователя
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("/")
            except IntegrityError:
                return render(request, 'wiki_app/signupuser.html',
                              {"form": UserCreationForm(), 'error': "Имя пользователя уже используется"})

        else:
            return render(request, 'wiki_app/signupuser.html',
                          {"form": UserCreationForm(), 'error': "Пароли не совпадают"})


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")


def loginuser(request):
    if request.method == "GET":
        return render(request, 'wiki_app/loginuser.html', {"form": AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, 'wiki_app/loginuser.html',
                          {"form": AuthenticationForm(), "error": "Имя пользователя или пароль некорректны"})
        else:
            login(request, user)
            return redirect("/")


def deletemessage(request, id_message):
    messages = get_object_or_404(Messages, pk=id_message)
    id = messages.id_company
    if request.method == "POST":
        messages.delete()
        return redirect(f"/company{id}/")
