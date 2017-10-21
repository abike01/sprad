import json
# from datetime import time
import random
import threading
from time import time

import sprad.oscript.project_sets as clP_s

import requests
from django.utils.timezone import now, pytz

from jangoPro import settings
from .Conn_DB import addMatches


class Tic:
    tic = None
    stop_timer = False


def tennisinfo_timer():
    if Tic.stop_timer == False:
        Tic.tic = time()
        Tic.stop_timer = True
        threadingTimer()


def threadingTimer():
    ps_o = clP_s.Varsets()
    thTr=threading.Timer(random.randint(ps_o.interval_rmin, ps_o.interval_rmax), threadingTimer)
    thTr.start()

    toc = time()
    print("====: call the link, int: ", random.randint(ps_o.interval_rmin, ps_o.interval_rmax),'sec, diff: ', toc - Tic.tic)
    tennisinfo_f()
    if toc-Tic.tic>ps_o.poll_time:
        thTr.cancel()
        Tic.stop_timer = False
        print("! cancel calls. ")
        return


def tennisinfo_f():
    '''
    json_rec = tennisinfo.objects.all()
    q1 = json_rec[0]
    s=''
    for q in json_rec:
        if s!='':
            s=s+', \n'
        s=s + q.gjson
    print(s)
    '''
    o_Tzone = pytz.timezone(settings.TIME_ZONE)  # GMT+1

    # now_date_str = datetime.datetime.now().strftime('%Y%m%d')
    now_date_str = now().astimezone(o_Tzone).strftime('%Y%m%d')
    ourUrl = 'https://ls.sportradar.com/ls/feeds/?/itf/en/Europe:Berlin/gismo/client_dayinfo/'
    ourUrl += now_date_str
    # ourUrl += '20170812'

    try:
        response = requests.get(ourUrl, timeout=(10, 10))
    except requests.exceptions.ConnectTimeout:
        print('Oops. Problems requests!')
        return None

    print(ourUrl)

    data = json.loads(response.content)
    json_data = json.dumps(None)
    jdata = []
    # {"queryUrl":"client_dayinfo\/20170729","doc":[{"event":
    my_list = data['doc'][0]['data']['matches']
    for ij in my_list:
        matchstatus = data['doc'][0]['data']['matches'][ij]['match']['matchstatus']
        if matchstatus == 'live':
            jdata.append(matchstatus_live(ij, matchstatus, data['doc'][0]['data']['matches'][ij],
                                          data['doc'][0]['data']['tournaments']))

            #    print('jdata: ', jdata, ' jdata.len= ', len(jdata))  # None
    if len(jdata) == 0:
        print('Oops. no data!')
        return None

    json_data = json.dumps(jdata)
    #    print('json_data: ', json_data, ' json_data.len= ', len(json_data))  # None
    tic = time()
    addMatches('jpro_tournaments', json_data)
    toc = time()
    print('diffTime: ', toc - tic)

    return 'Ok'


def matchstatus_live(ij, matchstatus, matches_ij, tournaments):  # data['doc'][0]['data']['matches'][ij]
    jdatal = {}
#gamescore
    jdatal['matches_id'] = ij
    jdatal['tid'] = matches_ij['match']['_tid']
    jdatal['matchstatus'] = matchstatus
    jdatal['param5'] = matches_ij['param5']
    jdatal['param10'] = matches_ij['param10']
    jdatal['param1'] = matches_ij['param1']
    jdatal['param2'] = matches_ij['param2']

    jdatal['mt_dt_time'] = matches_ij['match']['_dt']['time']
    jdatal['mt_dt_date'] = matches_ij['match']['_dt']['date']
    jdatal['mt_dt_tz'] = matches_ij['match']['_dt']['tz']
    jdatal['mt_dt_tzoffset'] = matches_ij['match']['_dt']['tzoffset']
    jdatal['mt_roundname_name'] = matches_ij['match']['roundname']['name']
    jdatal['mt_roundname_displaynumber'] = matches_ij['match']['roundname']['displaynumber']
    jdatal['mt_roundname_statisticssortorder'] = matches_ij['match']['roundname']['statisticssortorder']
    jdatal['mt_cuproundmatchnumber'] = matches_ij['match']['cuproundmatchnumber']
    jdatal['mt_cuproundnumberofmatches'] = matches_ij['match']['cuproundnumberofmatches']
    jdatal['mt_week'] = matches_ij['match']['week']
    jdatal['mt_coverage_lineup'] = matches_ij['match']['coverage']['lineup']
    jdatal['mt_coverage_formations'] = matches_ij['match']['coverage']['formations']
    jdatal['mt_coverage_livetable'] = matches_ij['match']['coverage']['livetable']
    jdatal['mt_coverage_injuries'] = matches_ij['match']['coverage']['injuries']
    jdatal['mt_coverage_ballspotting'] = matches_ij['match']['coverage']['ballspotting']
    jdatal['mt_coverage_cornersonly'] = matches_ij['match']['coverage']['cornersonly']
    jdatal['mt_coverage_multicast'] = matches_ij['match']['coverage']['multicast']
    jdatal['mt_coverage_scoutmatch'] = matches_ij['match']['coverage']['scoutmatch']
    jdatal['mt_coverage_scoutcoveragestatus'] = matches_ij['match']['coverage']['scoutcoveragestatus']
    jdatal['mt_coverage_scoutconnected'] = matches_ij['match']['coverage']['scoutconnected']
    jdatal['mt_coverage_liveodds'] = matches_ij['match']['coverage']['liveodds']
    jdatal['mt_coverage_deepercoverage'] = matches_ij['match']['coverage']['deepercoverage']
    jdatal['mt_coverage_tacticallineup'] = matches_ij['match']['coverage']['tacticallineup']
    jdatal['mt_coverage_basiclineup'] = matches_ij['match']['coverage']['basiclineup']
    jdatal['mt_coverage_hasstats'] = matches_ij['match']['coverage']['hasstats']
    jdatal['mt_coverage_inlivescore'] = matches_ij['match']['coverage']['inlivescore']
    jdatal['mt_coverage_advantage'] = matches_ij['match']['coverage']['advantage']
    jdatal['mt_coverage_tiebreak'] = matches_ij['match']['coverage']['tiebreak']
    jdatal['mt_coverage_penaltyshootout'] = matches_ij['match']['coverage']['penaltyshootout']
    jdatal['mt_coverage_scouttest'] = matches_ij['match']['coverage']['scouttest']
    jdatal['mt_coverage_lmtsupport'] = matches_ij['match']['coverage']['lmtsupport']
    jdatal['mt_coverage_venue'] = matches_ij['match']['coverage']['venue']
    jdatal['mt_coverage_matchdatacomplete'] = matches_ij['match']['coverage']['matchdatacomplete']
    jdatal['mt_coverage_mediacoverage'] = matches_ij['match']['coverage']['mediacoverage']
    jdatal['mt_coverage_paperscorecard'] = matches_ij['match']['coverage']['paperscorecard']
    jdatal['mt_result_home'] = matches_ij['match']['result']['home']
    jdatal['mt_result_away'] = matches_ij['match']['result']['away']
    jdatal['mt_result_winner'] = matches_ij['match']['result']['winner']
    # print('mt_periods: ', matches_ij['match']['periods'])
    jdatal['mt_periods'] = matches_ij['match']['periods']
    jdatal['mt_updated_uts'] = matches_ij['match']['updated_uts']
    jdatal['mt_p'] = matches_ij['match']['p']
    jdatal['mt_ptime'] = matches_ij['match']['ptime']
    # print('mt_timeinfo: ',matches_ij['match']['timeinfo'])
    jdatal['mt_timeinfo'] = matches_ij['match']['timeinfo']
    jdatal['mt_teams_home_name'] = matches_ij['match']['teams']['home']['name']
    try:
        jdatal['mt_teams_home_seed_seeding'] = matches_ij['match']['teams']['home']['seed']['seeding']
    except Exception:
        jdatal['mt_teams_home_seed_seeding'] = ''
    try:
        jdatal['mt_teams_home_seed_type_short'] = matches_ij['match']['teams']['home']['seed']['type_short']
    except Exception:
        jdatal['mt_teams_home_seed_type_short'] = ''
    jdatal['mt_teams_away_name'] = matches_ij['match']['teams']['away']['name']
    try:
        jdatal['mt_teams_away_seed_seeding'] = 'seeding', matches_ij['match']['teams']['away']['seed']['seeding']
    except Exception:
        jdatal['mt_teams_away_seed_seeding'] = ''
    try:
        jdatal['mt_teams_away_seed_type_short'] = matches_ij['match']['teams']['away']['seed']['type_short']
    except Exception:
        jdatal['mt_teams_away_seed_type_short'] = ''
    jdatal['mt_status_name'] = matches_ij['match']['status']['name']
    jdatal['mt_removed'] = matches_ij['match']['removed']
    jdatal['mt_facts'] = matches_ij['match']['facts']
    jdatal['mt_localderby'] = matches_ij['match']['localderby']
    jdatal['mt_hf'] = matches_ij['match']['hf']
    jdatal['mt_periodlength'] = matches_ij['match']['periodlength']
    jdatal['mt_numberofperiods'] = matches_ij['match']['numberofperiods']
    jdatal['mt_overtimelength'] = matches_ij['match']['overtimelength']
    jdatal['mt_bestofsets'] = matches_ij['match']['bestofsets']
    jdatal['mt_tobeannounced'] = matches_ij['match']['tobeannounced']
    jdatal['courtdisplayorder'] = matches_ij['courtdisplayorder']
    jdatal['islivescoringprovided'] = matches_ij['islivescoringprovided']
    #    print('matches_ij: ',matches_ij )
    #    print('tournaments: ', tournaments)

    for ijt in tournaments:
        if tournaments[ijt]['_id'] == matches_ij['match']['_tid']:
            jdatal['city'] = tournaments[ijt]['tennisinfo']['city']
            jdatal['gender'] = tournaments[ijt]['tennisinfo']['gender']
            jdatal['type'] = tournaments[ijt]['tennisinfo']['type']
            jdatal['kind_sport'] = 'tennis'
            jdatal['prize_amount'] = tournaments[ijt]['tennisinfo']['prize']['amount']
            jdatal['prize_currency'] = tournaments[ijt]['tennisinfo']['prize']['currency']
            jdatal['tourn_name'] = tournaments[ijt]['name']
            jdatal['ground_id'] = '001'#tournaments[ijt]['ground']['_id']
            jdatal['ground_mainid'] = '007'# tournaments[ijt]['ground']['mainid']
            jdatal['itfstartdate'] = tournaments[ijt]['itfstartdate']
            jdatal['itfenddate'] = tournaments[ijt]['itfenddate']

    return jdatal
