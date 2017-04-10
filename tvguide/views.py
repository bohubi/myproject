from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from django.utils.dateparse import parse_datetime
from django.utils.datetime_safe import datetime

from tvguide.models import *


def index(request):
    now = datetime.now()
    timeslots = TimeSlot.objects.filter(finish__gt=now).order_by('start')[0:8]
    context = {'timeslots':timeslots , 'now':now}

    # time_start = TimeSlot.objects.filter(start="2017-04-07 20:15:00")
    # time_list = Program.objects.filter(timeslot__start__gte=parse_datetime('2017-04-07 20:15:00'))
    # context = {
    #     "time_list": time_list,
    #     "time_start" : time_start}

    return render(request, "tvguide/index.html", context)

    # channel_list = Channel.objects.all()
    # program_list = Program.objects.all()
    # category_list = Category.objects.all()
    # time_slot_list= TimeSlot.objects.all()
    # genre_list= Genre.objects.all()
    # programgenre_list= ProgramGenre.objects.all()
    # context = {
    #     'channel_list': channel_list,
    #     'program_list': program_list,
    #     'category_list': category_list,
    #     'time_slot_list' : time_slot_list,
    #     'genre_list' : genre_list,
    #     'programgenre_list' : programgenre_list,
    # }
    #question_count = question_list.count()
    #return render(request, "tvguide/index.html", context)