from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.template import RequestContext


def home(request):
    return render(request, 'html/home.html', {
        'foo': 'bar',
    })


def games(request):
    return render(request, 'html/games.html', {
        'foo': 'bar',
    })


def login(request):
    return render(request, 'html/login.html', {
        'foo': 'bar',
    })

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def register(request):
    return render(request, 'html/register.html', {
        'foo': 'bar',
    })


def scoreboard(request):
    return render(request, 'html/scoreboard.html', {
        'foo': 'bar',
    })


def notification(request):
    return render(request, 'html/notifications.html', {
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
