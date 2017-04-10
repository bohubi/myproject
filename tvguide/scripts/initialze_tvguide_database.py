import os
import random

import django
import sys

from django.db.models import Max
from django.utils.dateparse import parse_datetime, parse_date
from math import floor

print('Python %s on %s' % (sys.version, sys.platform))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
print('Django version %s' % django.get_version())

from tvguide.models import Channel, Category, Program, TimeSlot, Genre, ProgramGenre

# delete everything


Channel.objects.all().delete()
TimeSlot.objects.all().delete()
Program.objects.all().delete()
ProgramGenre.objects.all().delete()
Category.objects.all().delete()
Genre.objects.all().delete()

# CHANNELS

mbc_channel = Channel(name='mbc')
mbc_channel.save()

mbc2 = Channel(name="MBC 2")
mbc2.save()

appletv_channel = Channel(name="AppleTV")
lbc_channel = Channel(name="LBC")
banana_channel = Channel(name="Banana")
whynot_channel = Channel(name="WhyNot")
you_channel = Channel(name="You")

appletv_channel.save()
lbc_channel.save()
banana_channel.save()
whynot_channel.save()
you_channel.save()

alarabia_channel = Channel(name="AlarabiaTV")
alarabia_channel.save()

ktv_channel = Channel(name="Kuwait TV")
ktv_channel.save()
mbcmax_channel = Channel(name="MBC MAX")
mbcmax_channel.save()
dubai_one_channel = Channel(name="Dubai One")
dubai_one_channel.save()
mbc2_channel = Channel(name="MBC 2")
mbc2_channel.save()
ktv2_channel = Channel(name="Kuwait TV 2")
ktv2_channel.save()


# CATEGORIES
movie_category = Category(name='Movie')
movie_category.save()

arabic_category = Category(name="Arabic")
pg13_category = Category(name="PG13")
pg12_category = Category(name="PG12")

arabic_category.save()
pg13_category.save()
pg12_category.save()

series_category = Category(name="Series")
series_category.save()

documentary_category = Category(name="Documentary")
documentary_category.save()
movies_category = Category(name="Movie")
movies_category.save()
news_category = Category(name="News")
news_category.save()
cat4 = Category(name="Series")
cat4.save()
talkshow_category = Category(name="Talk Show")
talkshow_category.save()


# GENRES

action_genre = Genre(name='Action')
action_genre.save()

horror_genre = Genre(name="Horror")
comedy_genre = Genre(name="Comedy")
action_genre = Genre(name="Action")

horror_genre.save()
comedy_genre.save()
action_genre.save()

pg_genre = Genre(name="PG")
pg_genre.save()

thriller_genre = Genre(name="Thriller")
thriller_genre.save()
comedy_genre = Genre(name="Comedy")
comedy_genre.save()
horror_genre = Genre(name="Horror")
horror_genre.save()
kids_genre = Genre(name="Kids")
kids_genre.save()
documentary_genre = Genre(name="Documentary")
documentary_genre.save()

# PROGRAMS

topgear_program = Program(
    name='Top Gear',
    duration_in_minutes=45,
    release_year=2012,
    category=movie_category)
topgear_program.save()

everybody_loves_raymond_program = Program(
    name="Everybody Loves Raymond",
    duration_in_minutes=300,
    release_year=2003,
    category=arabic_category,
)
everybody_loves_raymond_program.save()

seinfield_program = Program(
    name="Seinfield",
    duration_in_minutes=120,
    release_year=2005,
    category=pg13_category,
)

seinfield_program.save()

django_unleashed_program = Program(
    name="Django Unleashed",
    duration_in_minutes=220,
    release_year=2013,
    category=pg12_category,
)

django_unleashed_program.save()

third_rock_program = Program(name="thirdrock", duration_in_minutes=40, release_year=2003, category=series_category)
third_rock_program.save()

timezone_program = Program(name="timezone", duration_in_minutes=33, release_year=1998, category=documentary_category)
timezone_program.save()
supernatural_program = Program(name="Supernatural", duration_in_minutes=33, release_year=1998, category=cat4)
supernatural_program.save()
oprah_program = Program(name="Oprah", duration_in_minutes=33, release_year=1998, category=talkshow_category)
oprah_program.save()
exorcist_program = Program(name="The Exorcist", duration_in_minutes=33, release_year=1998, category=movies_category)
exorcist_program.save()
the_big_bang_program = Program(name="The Big Bang Theory", duration_in_minutes=33, release_year=1998, category=cat4)
the_big_bang_program.save()


# PROGRAM GENRES

ProgramGenre(program=topgear_program, genre=action_genre).save()

ProgramGenre(
    program=everybody_loves_raymond_program,
    genre=comedy_genre,
).save()

ProgramGenre(
    program=seinfield_program,
    genre=horror_genre,
).save()

ProgramGenre(program=third_rock_program, genre=pg_genre).save()

ProgramGenre(program=timezone_program, genre=documentary_genre).save()
ProgramGenre(program=supernatural_program, genre=thriller_genre).save()
ProgramGenre(program=oprah_program, genre=documentary_genre).save()
ProgramGenre(program=exorcist_program, genre=horror_genre).save()
ProgramGenre(program=the_big_bang_program, genre=comedy_genre).save()

# TIMESLOTS

TimeSlot(
    start=parse_datetime('2012-02-01 23:00:00'),
    finish=parse_datetime('2012-02-01 23:59:00'),
    channel=mbc_channel,
    program=topgear_program
).save()

TimeSlot(
    start=parse_date("2012-02-11"),
    finish=parse_date("2012-02-12"),
    channel=appletv_channel,
    program=everybody_loves_raymond_program,
).save()

TimeSlot(
    start=parse_date("2012-02-11"),
    finish=parse_date("2012-02-12"),
    channel=lbc_channel,
    program=everybody_loves_raymond_program,
).save()

TimeSlot(start=parse_datetime("2016-09-12 21:09:01"), finish=parse_datetime("2016-09-12 21:49:01"),
         channel=alarabia_channel, program=third_rock_program).save()

TimeSlot(start="2012-03-01", finish="2012-03-01", channel=ktv_channel, program=timezone_program).save()
TimeSlot(start="2012-06-05", finish="2012-06-05", channel=mbcmax_channel, program=supernatural_program).save()
TimeSlot(start="2012-02-06", finish="2012-02-06", channel=dubai_one_channel, program=oprah_program).save()
TimeSlot(start="2012-02-07", finish="2012-02-07", channel=mbc2_channel, program=exorcist_program).save()
TimeSlot(start="2012-05-08", finish="2012-05-08", channel=ktv2_channel, program=the_big_bang_program).save()


# RANDOM INSERTIONS

def assign_random_program_genre():
    program = random.choice(Program.objects.all())
    genre = random.choice(Genre.objects.all())
    if ProgramGenre.objects.filter(program=program, genre=genre).count() == 0:
        ProgramGenre(program=program, genre=genre).save()


for i in range(1, 10):
    assign_random_program_genre()


def assign_random_slots():
    import datetime

    def next_slot_time(t):
        t = t + datetime.timedelta(minutes=14, seconds=59, microseconds=999999)
        t = t.replace(microsecond=0, second=0, minute=floor(t.minute / 15) * 15)
        return t

    program = random.choice(Program.objects.all())
    channel = random.choice(Channel.objects.all())
    start_time = TimeSlot.objects.filter(channel=channel).aggregate(Max('finish'))['finish__max'];
    if start_time is None:
        start_time = datetime.datetime.now()

    start_time = next_slot_time(start_time)
    finish_time = next_slot_time(start_time + datetime.timedelta(minutes=program.duration_in_minutes * 1.1))
    print("%s -> %s (%d minutes)" % (start_time, finish_time, program.duration_in_minutes))
    TimeSlot(
        start=start_time,
        finish=finish_time,
        channel=channel,
        program=program
    ).save()


def assign_random_slots2():
    import datetime

    program = random.choice(Program.objects.all())
    channel = random.choice(Channel.objects.all())

    def next_slot_time(t):
        t = t + datetime.timedelta(minutes=14, seconds=59, microseconds=999999)
        t = t.replace(microsecond=0, second=0, minute=floor(t.minute / 15) * 15)
        return t

    def time_is_used(t0, t1):
        return (TimeSlot.objects.filter(channel=channel, start__lt=t1, start__gte=t0).exists()
                or
                TimeSlot.objects.filter(channel=channel, start__lte=t0, finish__gt=t0).exists())

    start_time = next_slot_time(datetime.datetime.now() + datetime.timedelta(minutes=random.randint(0, 60 * 24 * 7)))
    finish_time = next_slot_time(start_time + datetime.timedelta(minutes=program.duration_in_minutes * 1.1))
    if not time_is_used(start_time, finish_time):
        TimeSlot(
            start=start_time,
            finish=finish_time,
            channel=channel,
            program=program
        ).save()


for i in range(1, 150):
    assign_random_slots2()

# print results

print("%d channels" % Channel.objects.count())
print("%d categories" % Category.objects.count())
print("%d genres" % Genre.objects.count())
print("%d programs" % Program.objects.count())
print("%d program genres" % ProgramGenre.objects.count())
print("%d timeslots" % TimeSlot.objects.count())