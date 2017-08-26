import json
from .Conn_DB import get_connection


def getFromTournaments():
    conn = get_connection('db.sqlite3')
    #conn = db.connect('db.sqlite3')
    sql = 'SELECT matches_id f1,tid f2,param5 f3 FROM jpro_tournaments group by tid ORDER BY tid'  # where matchstatus=\'live\'
    cursor = conn.cursor()
    cursor.execute(sql)

    columns = ('f1', 'f2', 'f3')
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    jres = json.dumps(results, indent=2)

    return jres

'''
register = template.Library()
@register.inclusion_tag('templates/jpro/jonny_base.html')
'''

def GetMatchesJlistJ(matcheId):
#    conn = db.connect('db.sqlite3')
    conn = get_connection('db.sqlite3')
    sql = 'SELECT t.matches_id f1, t.param5 f3, t.gender f2 FROM jpro_tournaments t' \
          ' WHERE t.tid in ( select tid from jpro_tournaments where matches_id IN (' + matcheId + '))'
#    print(sql)
    cursor = conn.cursor()

    cursor.execute(sql)

    columns = ('f1', 'f2', 'f3')
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    jres = json.dumps(results, indent=2)

    '''
    MatchDetailsJ =cursor.fetchall()
    jres = json.dumps(MatchDetailsJ, indent=2)
   '''
 #   print(jres)
    return jres
    pass


def GetMatchDetailsJ(matcheId):
#    conn = db.connect('db.sqlite3')
    conn = get_connection('db.sqlite3')
    sql = 'SELECT t.param1, t.mt_dt_date, t.mt_dt_time,t.mt_roundname_name,t.mt_roundname_statisticssortorder,t.mt_coverage_tiebreak,' \
          't.mt_result_home,t.mt_result_away,t.mt_result_winner,t.mt_timeinfo,t.mt_teams_home_name,t.mt_teams_away_name,' \
          't.mt_teams_away_seed_type_short,t.mt_status_name,t.mt_hf,t.mt_hf FROM match_details t' \
          ' WHERE t.matches_id IN (' + matcheId + ')'
#    print(sql)
    cursor = conn.cursor()

    cursor.execute(sql)
    MatchDetailsJ = cursor.fetchall()

    jres = json.dumps(MatchDetailsJ, indent=2)
#    print(jres)
    return jres
    #    return {'MatchDetailsJ': jres}
    pass

