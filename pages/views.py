from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *


def set_cookie(request):
    request.session['agree'] = 'ok'
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def page(request,name_slug):
    addClass = True
    settings = Settings.objects.first()
    header = Header.objects.first()
    feedbacks = Feedback.objects.all()
    block7 = Block7.objects.first()
    content = get_object_or_404(Page, name_slug =name_slug)
    pages = Page.objects.filter(is_active=True)
    return render(request, 'page.html', locals())

def implementation(request):
    settings = Settings.objects.first()
    pages = Page.objects.filter(is_active=True)
    header = Header.objects.first()
    return render(request, 'implementation.html', locals())


def instructions(request):
    pages = Page.objects.filter(is_active=True)
    settings = Settings.objects.first()
    header = Header.objects.first()
    return render(request, 'instructions.html', locals())

def terms(request):
    pages = Page.objects.filter(is_active=True)
    settings = Settings.objects.first()
    header = Header.objects.first()
    return render(request, 'terms.html', locals())

def tariffs(request):
    pages = Page.objects.filter(is_active=True)
    settings = Settings.objects.first()
    header = Header.objects.first()
    return render(request, 'tariffs.html', locals())


def index(request):
    indexPage = True
    settings = Settings.objects.first()
    header = Header.objects.first()
    block1 = Block1.objects.first()
    block2 = Block2.objects.first()
    block3 = Block3.objects.first()
    block4 = Block4.objects.first()
    block5 = Block5.objects.first()
    block6 = Block6.objects.first()
    block7 = Block7.objects.first()
    feedbacks = Feedback.objects.all()
    pages = Page.objects.filter(is_active=True)

    return render(request, 'index.html', locals())