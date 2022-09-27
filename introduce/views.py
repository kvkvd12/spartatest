from django.shortcuts import render
from .models import AccessLog

def introduce(request):
    access_log = AccessLog()
    access_log.location = "introduce"
    access_log.save()

    # AccessLog.objects.create()

    return render(request, 'test_introduce.html')
