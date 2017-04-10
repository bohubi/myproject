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

#pp(Channel.objects.all())
#pp(Program.objects.filter(duration_in_minutes=33))
#pp(Program.objects.filter(duration_in_minutes=33).count())
#pp(Program.objects.filter(name__startswith="t"))
#pp(Program.objects.filter(name__startswith="t",name__endswith="x"))
#pp(Program.objects.filter(release_year=1998).order_by('name')[3])
#pp(Program.objects.exclude(name__contains="c").filter(release_year=1998).count())
#prog=(Program.objects.exclude(name__contains="c").filter(release_year=1998).count())

#to get all the programs with category name is movie
#cat = Category.objects.filter(name="Movie")

#pp(Program.objects.filter(category=cat))

#We want to get all the timeslots in mbc channel and program category contains movie
#pp(TimeSlot.objects.filter(channel__name__contains="mbc",program__category__name__contains="Movie"))
#pp(TimeSlot.objects.filter(channel__name__contains="mbc",program__category__name__contains="Movie").count())

#pp(TimeSlot.objects.filter(channel__name__contains="ba", program__duration_in_minutes__gt=30, program__release_year__gt=2000, program__category__name__contains="ie",start__week_day=5).only('id'))

#pp(Program.objects.aggregate(Min('duration_in_minutes')))
#pp(Category.objects.annotate(Sum('program__duration_in_minutes')))
#pp(Category.objects.annotate(Count('program__timeslot')))
#pp(Genre.objects.annotate(Count('programgenre__program')))
##pp(Program.objects.annotate(Count('programgenre')).aggregate(Avg('programgenre__count')))
pp(Program.objects.filter(timeslot__start__gte=parse_datetime('2017-04-07 20:30:00')))


        #print(Channel.objects.count())
#print(Channel.objects.all())