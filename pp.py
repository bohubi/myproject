import os
import random

import django
import sys

from django.db.models import Max, Sum, Avg, Min, Count
from django.utils.dateparse import parse_datetime, parse_date
from math import floor

print('Python %s on %s' % (sys.version, sys.platform))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
print('Django version %s' % django.get_version())

from tvguide.models import Channel, Category, Program, TimeSlot, Genre, ProgramGenre

def pp(x):
    import pprint, json
    from django.db.models import QuerySet, Model

    def objectify(x):
        d = {}
        for p in x.__dict__:
            if not p.startswith("_"):
                d[p] = x.__dict__[p]
        return d

    if isinstance(x, QuerySet):
        print(x.query)
        pprint.pprint([objectify(y) for y in x])
    elif isinstance(x, Model):
        pprint.pprint(objectify(x))
    else:
        pprint.pprint(x)