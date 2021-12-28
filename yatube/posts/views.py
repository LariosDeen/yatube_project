from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница сайта.')


def group_posts(request, slug):
    return HttpResponse(f'Здесь будут посты, отфильтрованные по группе {slug}.')
