# from urllib import request
# from django.http import HttpResponse
# from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied

import sprad.oscript.get_json01 as get_json01
import sprad.oscript.set_respons as setRes


def GetTournamentsJlist():
    print('GetTournamentsJlist')
    get_json01.tennisinfo_timer() #tennisinfo_f()   # получает Json и заполняет оператвиную таблицу jpro_tournaments
    tournaments_lst = setRes.getFromTournaments()  # выдает список турниров из таблицы jpro_tournaments
    return tournaments_lst


def GetMatchesJlist(matcheId):  # выдает список матчей данного турнира, из таблицы jpro_tournaments
    MatchDetailsJ = setRes.GetMatchesJlistJ(matcheId)
    return MatchDetailsJ


def GetMatchDetails(matcheId, requestU):  # выдает детали матча из таблицы jpro_tournaments
    if requestU.user.is_authenticated():
        print('is_authenticated: ', requestU.user.is_authenticated())
        MatchDetailsJ = setRes.GetMatchDetailsJ(matcheId)
        return MatchDetailsJ
    else:
        print('NOT is_authenticated!!! ', requestU.user)
        return None


def authenticateOurUser(requestU):
    username = requestU.GET.get('userdj')
    password = requestU.GET.get('passworddj')
    user = authenticate(username=username, password=password)
    if user is not None:
        try:
            login(requestU, user)
        except PermissionDenied:
            return 'error' #HttpResponse('None', content_type='text/html')
    else:
        return None # HttpResponse('None', content_type='text/html')
    return username


def authorizationSave(requestU):
    from django.contrib.auth.models import User
    username = requestU.GET.get('userdj')
    password = requestU.GET.get('passworddj')
    email = requestU.GET.get('email')
    print('authnews!!! username: ', username, ' password: ', password, ' email: ', email)

    if User.objects.filter(username=username).exists():
        return 'y'
    else:
        user = User.objects.create_user(username, email, password);
        '''
        user.user_permissions = '2'
        user.save()
        '''
    print('authorizationSave')
    pass
