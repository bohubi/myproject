from datetime import datetime

import os
import django
import sys

from django.utils.dateparse import parse_date, parse_datetime

print('Python %s on %s' % (sys.version, sys.platform))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
print('Django version %s' % django.get_version())

from tvguide.models import Channel, Category, Program, TimeSlot, Genre, ProgramGenre

Channel.objects.all().delete()
Category.objects.all().delete()
Program.objects.all().delete()
TimeSlot.objects.all().delete()
Genre.objects.all().delete()
ProgramGenre.objects.all().delete()

channel1=Channel(name="AlarabiaTV")
channel1.save()

category1=Category(name="Series")
category1.save()

program1= Program(name="thirdrock", duration_in_minutes=40, release_year=2003, category=category1)
program1.save()

timeslot1=TimeSlot(start= parse_datetime("2016-09-12 21:09:01"), finish=parse_datetime("2016-09-12 21:49:01"), channel=channel1, program=program1)
timeslot1.save()

genre1=Genre(name="PG")
genre1.save()

ProgramGenre(program=program1, genre=genre1).save()

print("%d Channel in the database" % Channel.objects.count())
print("%d  Category in the database" % Category.objects.count())
print("%d  Program in the database" % Program.objects.count())
print("%d TimeSlot in the database" % TimeSlot.objects.count())
print("%d Genre in the database" % Genre.objects.count())
print("%d ProgramGenre in the database" % ProgramGenre.objects.count())
