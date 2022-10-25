import os

os.environ.setdefault( 'DJANGO_SETTINGS_MODULE','dsctf.settings' )
import django

django.setup()
from CTF.models import *
user = User.objects.all()
print(user)