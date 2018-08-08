from django.shortcuts import render


def record(request):
    return render(request, 'studio/pages/record.html')


def mix(request):
    return render(request, 'studio/pages/web-audio-editor.html')
