import os
import django
import sys

from django.contrib.auth import authenticate
from django.utils.dateparse import parse_date

from pp import pp

print('Python %s on %s' % (sys.version, sys.platform))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

print('Django version %s' % django.get_version())

from django.contrib.auth.models import User
#pp(User.objects.all())

#User.objects.create_user("john3", "join@foo.com","jp")

#user = User.objects.get(username="john2")
#pp(user)

#to check if the password is right or not (True or False)
#pp(user.check_password("jp"))


user = authenticate(username="john2", password="jp")
if user is None:
    print("Invalid")
else:
    print("Hello" + user.username)