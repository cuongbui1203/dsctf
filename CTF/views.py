from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from CTF.forms import *
import datetime
from django.template import RequestContext
from django.http import HttpResponseRedirect

from API.views import *
def home(request):
    form = MatchForm()
    return render(request, 'html/home.html', {
        'y': range(5),
        'form':form,
        'matchs': MATCH
    })


def users(request):
    users = User.objects.all()
    return render(request, 'html/users.html', {
        'users': users,
    })


def games(request):
    games = Game.objects.all()
    return render(request, 'html/games.html', {'games': games})


def create_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            gameIP = form.cleaned_data.get('gameIP')
            gamePort = form.cleaned_data.get('gamePort')
            gameName = form.cleaned_data.get('gameName')
            gameRule = form.cleaned_data.get('gameRule')
            author = form.cleaned_data.get('author')
            if Game.objects.filter(gameIP=gameIP, gamePort=gamePort).first() is None:
                try:
                    game = Game(gameIP=gameIP, gamePort=gamePort, gameName=gameName, gameRule=gameRule, author=author)
                    print(game)
                    game.save()
                    messages.info(request, f"create successful {gameName} game.")
                except Exception as e:
                    print(e)
                    messages.info(request, f"Game {gameName} creation failed.")
                return redirect("ctf:games")
            else:
                messages.error(request,f"{gameIP} already exists")

    form = GameForm()
    return render(request, 'html/creategame.html', {'game_form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("ctf:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="html/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("ctf:login")


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = (form.cleaned_data.get('username'))
            email = (form.cleaned_data.get('email'))
            password = (form.cleaned_data.get('password1'))

            if User.objects.filter(email=email).first() is None:
                user = User(email=email, username=username)
                print(password)
                user.set_password(password)
                print(user.password)
                user.save()
                messages.info(request, u'The account "%s" has been successfully registered.' % email)
                return redirect("ctf:login")
            else:
                messages.error(request, u'Email "%s" is already in use.' % email)
    else:
        form = NewUserForm()
    return render(request=request, template_name="html/register.html", context={"register_form": form})


def scoreboard(request):
    users = User.objects.order_by('-userScore').all()
    return render(request, 'html/scoreboard.html', {
        'users': users,
    })


def notification(request):
    return render(request, 'html/notifications.html', {
        'foo': 'bar',
    })


def profile(request):
    return render(request, 'html/profile.html', {
        'foo': 'bar',
    })


def admin(request):
    return render(request, 'html/admin.html', {
        'foo': 'bar',
    })


def handler404(request, *args, **argv):
    response = render(request, 'html/404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, 'html/500.html', {})
    response.status_code = 500
    return response
