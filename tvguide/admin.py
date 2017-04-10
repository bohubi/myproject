

# Register your models here.
from django.contrib import admin

from tvguide.models import *

admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(Program)
admin.site.register(TimeSlot)
admin.site.register(Genre)
admin.site.register(ProgramGenre)