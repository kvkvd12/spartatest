from django.shortcuts import render

def introduce(request):
    return render(request, 'test_introduce.html')