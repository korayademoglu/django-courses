from django.shortcuts import render
from django.http import HttpResponse


def home(req):
    return HttpResponse('anasayfa')
def kurslar(req):
    return HttpResponse('kurs listesi')

def getCoursesByCategory(req,cat):
    return HttpResponse(f'{cat} sayfasını getir')
