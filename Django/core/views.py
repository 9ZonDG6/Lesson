from django.http import HttpResponse
import datetime


def time(request):
    return HttpResponse(datetime.datetime.now())
