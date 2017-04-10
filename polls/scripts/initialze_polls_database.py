import os
import django
import sys

from django.utils.dateparse import parse_date

print('Python %s on %s' % (sys.version, sys.platform))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
print('Django version %s' % django.get_version())

from polls.models import Question, Choice

Question.objects.all().delete()
Choice.objects.all().delete()

q = Question(question_text="What's your favorite color?", pub_date=parse_date("2012-02-01"))
q.save()

Choice(choice_text="Green", question=q).save()
Choice(choice_text="red", question=q).save()
Choice(choice_text="blue", question=q).save()
Choice(choice_text="white", question=q).save()

q = Question(question_text="What's your favorite programming language?", pub_date=parse_date("2012-02-01"))
q.save()
Choice(choice_text="Python", question=q).save()
Choice(choice_text="Java", question=q).save()
Choice(choice_text="C++", question=q).save()
Choice(choice_text="Ruby", question=q).save()
Choice(choice_text="PHP", question=q).save()


print("%d questions in the database" % Question.objects.count())
print("%d choices in the database" % Choice.objects.count())
