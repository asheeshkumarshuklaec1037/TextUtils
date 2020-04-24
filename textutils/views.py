from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed+= char
        params = {'purpose':'Remove Punctuation', 'analyzed_text':analyzed }
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose':'Changed to uppercase', 'analyzed_text':analyzed }
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed+=char
        params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed }
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed+=char
        params = {'purpose':'Extra Spaces Removed', 'analyzed_text':analyzed }
        djtext = analyzed

    if charcounter == 'on':
        analyzed = len(djtext)
        params = {'purpose':'Total character count', 'analyzed_text':analyzed }
        djtext = analyzed
    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcounter != 'on':
        return HttpResponse('Error!!! Please select atleast one operation')

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')