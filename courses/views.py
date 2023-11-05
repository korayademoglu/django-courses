from django.shortcuts import redirect, render
from django.http import HttpResponse


def home(req):
    return HttpResponse('<h1>kurslar anasayfa</h1>')
def kurslar(req):
    return HttpResponse('kurs listesi')
def test(req):
    return render(req,'test.html')

def getCoursesByCategory(req,cat):
    return HttpResponse(f'{cat} sayfasını getir')
def youtubeLink(req):
    return redirect('https://www.youtube.com')
