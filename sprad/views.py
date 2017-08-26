#from django.contrib import auth
#import UserProfile as UserProfile

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import sprad.oscript.dispetch_controller as dc
from django.contrib.auth import authenticate, login , logout


def jonny(request):
    return render(request, 'sprad_tmpls/janix.html', {})


def controller(request):
    if request.method == "GET":
        if request.GET.get('par1'):
            print('controller')
            tournamentsJlist = dc.GetTournamentsJlist()
            return HttpResponse(tournamentsJlist, content_type='text/html')

        reqGet = request.GET.get('tid')
        if request.GET.get('tid'):
            if reqGet != '':
                MatchDetailsJList = dc.GetMatchesJlist(reqGet)
                return HttpResponse(MatchDetailsJList, content_type='text/html')

        reqGet = request.GET.get('mid')
        if reqGet:
            if reqGet != '':
                MatchDetailsJList = dc.GetMatchDetails(reqGet, request)
                if MatchDetailsJList == None:
                    return render(request, 'sprad_tmpls/authoriz.html', {}) #вывод формы авторизации
                return HttpResponse(MatchDetailsJList, content_type='text/html')
    else:
        return HttpResponse('None', content_type='text/html')


def authorization(request):
    if request.GET.get('logout'):
        logout(request)
        return render(request, 'sprad_tmpls/janix.html', {})

    if request.GET.get('authnew'): # У вас нет аккаунта? Регистрация (вывод формы регистрации)
        print('authnew_form: ',request.GET.get('authnew'))
        return render(request, 'sprad_tmpls/registrate.html', {})

    if request.GET.get('authnews'): # сохранение нового пользователя
        if dc.authorizationSave(request) == 'y':
            return HttpResponse('y', content_type='text/html')

    retAuth =dc.authenticateOurUser(request) # Авторизация на сайте
    if retAuth == 'error':
        return HttpResponse('None', content_type='text/html')
    if retAuth == None:
        print('Invalid login or password.')
        return HttpResponse('None', content_type='text/html')
    print(retAuth)
    return HttpResponse(retAuth, content_type='text/html')
