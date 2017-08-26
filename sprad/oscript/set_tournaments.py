import json
from time import strftime, gmtime

from datetime import datetime


def RealizTournaments(cursor, conn, jdata):
    #    print('data is commit begin: ', strftime("%Y-%m-%d %H:%M:%S:%m", gmtime()))
    jdata = json.loads(jdata)

    TournamentsArc(conn, cursor, jdata)
    recsIns = 0
    for ji in jdata:
        recsIns = recsIns + jpro_tournaments_insert(cursor, ji)

    conn.commit()
    #    print('data is commit end: ', strftime("%Y-%m-%d %H:%M:%S:%m", gmtime()), '  recsIns: ', recsIns)
    print('  recsIns: ', recsIns)
    pass


def TournamentsArc(conn, cursor, jdata):
    wheres = ''
    for il in jdata:
        wheres += il['matches_id'] + ","

    wheres = ' WHERE matches_id not in (' + wheres[:-1] + ')'

    sql = 'replace into tournaments_arc select * from jpro_tournaments' + wheres
    cursor.execute(sql)
    # conn.commit()
    sql = 'delete from jpro_tournaments' + wheres
    cursor.execute(sql)

    sql = 'delete from match_details' + wheres
    cursor.execute(sql)
    conn.commit()


def jpro_tournaments_insert(cursor, ji):
    recsIns = 0

    sql = 'INSERT INTO jpro_tournaments'
    sql += ' SELECT ' + str(ji['matches_id']) + ','
    sql += str(ji['tid']) + ','
    sql += '\'' + ji['matchstatus'] + '\','
    sql += '\'' + ji['param5'] + '\','
    sql += '\'' + ji['param10'] + '\','
    sql += '\'' + ji['gender'] + '\','
    sql += '\'' + ji['type'] + '\','
    sql += '\'' + ji['kind_sport'] + '\','
    sql += '\'' + ji['tourn_name'] + '\','
    sql += '\'' + ji['ground_id'] + '\','
    sql += '\'' + ji['ground_mainid'] + '\','
    sql += '\'' + ji['itfstartdate'] + '\','
    sql += '\'' + ji['itfenddate'] + '\''
    sql += ' WHERE NOT EXISTS(SELECT 1 FROM jpro_tournaments WHERE'
    sql += ' matches_id=' + str(ji['matches_id']) + ')'
    res = cursor.execute(sql)
    recsIns = recsIns + res.rowcount

    sql = 'replace into match_details values ('
    sql += ji['matches_id'] + ','
    sql += '\'' + ji['param1'] + '\','
    sql += '\'' + ji['param2'] + '\','
    sql += '\'' + ji['city'] + '\','
    sql += '\'' + ji['prize_amount'] + '\','
    sql += '\'' + ji['prize_currency'] + '\','
    sql += '\'' + ji['mt_dt_time'] + '\','
    sql += '\'' + str(datetime.strptime(ji['mt_dt_date'], '%y/%m/%d')) + '\','
    sql += '\'' + ji['mt_dt_tz'] + '\','
    sql += '\'' + str(ji['mt_dt_tzoffset']) + '\','
    sql += '\'' + ji['mt_roundname_name'] + '\','
    sql += '\'' + str(ji['mt_roundname_displaynumber']) + '\','
    sql += '\'' + str(ji['mt_roundname_statisticssortorder']) + '\','
    sql += '\'' + str(ji['mt_cuproundmatchnumber']) + '\','
    sql += '\'' + str(ji['mt_cuproundnumberofmatches']) + '\','
    sql += '\'' + str(ji['mt_week']) + '\','
    sql += '\'' + str(ji['mt_coverage_lineup']) + '\','
    sql += '\'' + str(ji['mt_coverage_formations']) + '\','
    sql += '\'' + str(ji['mt_coverage_livetable']) + '\','
    sql += '\'' + str(ji['mt_coverage_injuries']) + '\','
    sql += '\'' + str(ji['mt_coverage_ballspotting']) + '\','
    sql += '\'' + str(ji['mt_coverage_cornersonly']) + '\','
    sql += '\'' + str(ji['mt_coverage_multicast']) + '\','
    sql += '\'' + str(ji['mt_coverage_scoutmatch']) + '\','
    sql += '\'' + str(ji['mt_coverage_scoutcoveragestatus']) + '\','
    sql += '\'' + str(ji['mt_coverage_scoutconnected']) + '\','
    sql += '\'' + str(ji['mt_coverage_liveodds']) + '\','
    sql += '\'' + str(ji['mt_coverage_deepercoverage']) + '\','
    sql += '\'' + str(ji['mt_coverage_tacticallineup']) + '\','
    sql += '\'' + str(ji['mt_coverage_basiclineup']) + '\','
    sql += '\'' + str(ji['mt_coverage_hasstats']) + '\','
    sql += '\'' + str(ji['mt_coverage_inlivescore']) + '\','
    sql += '\'' + str(ji['mt_coverage_advantage']) + '\','
    sql += '\'' + str(ji['mt_coverage_tiebreak']) + '\','
    sql += '\'' + str(ji['mt_coverage_penaltyshootout']) + '\','
    sql += '\'' + str(ji['mt_coverage_scouttest']) + '\','
    sql += '\'' + str(ji['mt_coverage_lmtsupport']) + '\','
    sql += '\'' + str(ji['mt_coverage_venue']) + '\','
    sql += '\'' + str(ji['mt_coverage_matchdatacomplete']) + '\','
    sql += '\'' + str(ji['mt_coverage_mediacoverage']) + '\','
    sql += '\'' + str(ji['mt_coverage_paperscorecard']) + '\','
    sql += '\'' + str(ji['mt_result_home']) + '\','
    sql += '\'' + str(ji['mt_result_away']) + '\','
    sql += '\'' + str(ji['mt_result_winner']) + '\','
    #    sql +='\''+str(ji['mt_periods'])+'\','
    sql += '\'' + prepairField(ji['mt_periods']) + '\','
    sql += '\'' + str(ji['mt_updated_uts']) + '\','
    sql += '\'' + str(ji['mt_p']) + '\','
    sql += '\'' + str(ji['mt_ptime']) + '\','
    #    sql +='\''+str(ji['mt_timeinfo'])+'\','
    sql += '\'' + prepairField(ji['mt_timeinfo']) + '\','
    sql += '\'' + str(ji['mt_teams_home_name']) + '\','
    sql += '\'' + prepairField(ji['mt_teams_home_seed_seeding']) + '\','
    sql += '\'' + str(ji['mt_teams_home_seed_type_short']) + '\','
    sql += '\'' + str(ji['mt_teams_away_name']) + '\','
    sql += '\'' + prepairField(ji['mt_teams_away_seed_seeding']) + '\','
    sql += '\'' + str(ji['mt_teams_away_seed_type_short']) + '\','
    sql += '\'' + str(ji['mt_status_name']) + '\','
    sql += '\'' + str(ji['mt_removed']) + '\','
    sql += '\'' + str(ji['mt_facts']) + '\','
    sql += '\'' + str(ji['mt_localderby']) + '\','
    sql += '\'' + str(ji['mt_hf']) + '\','
    sql += '\'' + str(ji['mt_periodlength']) + '\','
    sql += '\'' + str(ji['mt_numberofperiods']) + '\','
    sql += '\'' + str(ji['mt_overtimelength']) + '\','
    sql += '\'' + str(ji['mt_bestofsets']) + '\','
    sql += '\'' + str(ji['mt_tobeannounced']) + '\','
    sql += '\'' + str(ji['islivescoringprovided']) + '\''
    sql += ')'
    sql = sql.replace('False','')
    sql = sql.replace('True', 'Y')
    #print(sql)
    cursor.execute(sql)

    return recsIns


def prepairField(p1):

    if p1:
        str1 = str(p1)
        str1 = str1.replace('\'', '"')
    else:
        return ''

    return str1


'''
def jpro_tournaments_update(cursor,ji):
    recsUpd = 0
    sql = 'update jpro_tournaments'
    sql += ' SET matches_id=' + str(ji['matches_id']) + ','
    sql += 'tid=\'' + str(ji['tid']) + '\','
    sql += 'matchstatus=\'' + ji['matchstatus'] + '\','
    sql += 'param5=\'' + ji['param5'] + '\','
    sql += 'param10=\'' + ji['param10'] + '\','
    sql += 'city=\'' + ji['city'] + '\','
    sql += 'gender=\'' + ji['gender'] + '\','
    sql += 'type=\'' + ji['type'] + '\','
    sql += 'kind_sport=\'' + ji['kind_sport'] + '\','
    sql += 'prize_amount=\'' + ji['prize_amount'] + '\','
    sql += 'prize_currency=\'' + ji['prize_currency'] + '\','
    sql += 'itfid=\'' + ji['itfid'] + '\','
    sql += 'tourn_name=\'' + ji['tourn_name'] + '\','
    sql += 'ground_id=\'' + ji['ground_id'] + '\','
    sql += 'ground_name=\'' + ji['ground_name'] + '\','
    sql += 'ground_mainid=\'' + ji['ground_mainid'] + '\','
    sql += 'ground_main=\'' + ji['ground_main'] + '\''
    sql += ' WHERE matches_id=' + str(ji['matches_id'])#+' and matchstatus=\'live\''
    #print(sql)
    res = cursor.execute(sql)
    recsUpd = recsUpd + res.rowcount
    return  recsUpd
'''
'''
    sql='insert into jpro_tournaments ' \
    '(matches_id,tid,matchstatus,param5,param10,city,gender,type,kind_sport,prize_amount,prize_currency,' \
    'itfid,tourn_name,ground_id,ground_name,ground_mainid,ground_main)'  \
    ' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

#    jdata=json.loads(jdata)
    my_list = jdata
    for ji in jdata:
        cursor.execute(sql,
                       (ji['matches_id'],
                        ji['tid'],
                        ji['matchstatus'],
                        ji['param5'],
                        ji['param10'],
                        ji['city'],
                        ji['gender'],
                        ji['type'],
                        ji['kind_sport'],
                        ji['prize_amount'],
                        ji['prize_currency'],
                        ji['itfid'],
                        ji['tourn_name'],
                        ji['ground_id'],
                        ji['ground_name'],
                        ji['ground_mainid'],
                        ji['ground_main']
                        )
                       )
        conn.commit()
#    results = cursor.fetchall()
'''

'''
    sql='replace into match_details ' \
    '(matches_id,param1,param2,city,prize_amount,prize_currency,mt_dt_time,mt_dt_date,mt_dt_tz,mt_dt_tzoffset,' \
    'mt_roundname_name,mt_roundname_displaynumber,mt_roundname_statisticssortorder,mt_cuproundmatchnumber,' \
    'mt_cuproundnumberofmatches,mt_week,mt_coverage_lineup,mt_coverage_formations,mt_coverage_livetable,' \
    'mt_coverage_injuries,mt_coverage_ballspotting,mt_coverage_cornersonly,mt_coverage_multicast,'\
    'mt_coverage_scoutmatch,mt_coverage_scoutcoveragestatus,mt_coverage_scoutconnected,mt_coverage_liveodds,' \
    'mt_coverage_deepercoverage,mt_coverage_tacticallineup,mt_coverage_basiclineup,mt_coverage_hasstats,' \
    'mt_coverage_inlivescore,mt_coverage_advantage,mt_coverage_tiebreak,mt_coverage_penaltyshootout,' \
    'mt_coverage_scouttest,mt_coverage_lmtsupport,mt_coverage_venue,mt_coverage_matchdatacomplete,' \
    'mt_coverage_mediacoverage,mt_coverage_paperscorecard,mt_result_home,mt_result_away,mt_result_winner,' \
    'mt_periods,mt_updated_uts,mt_p,mt_ptime,mt_timeinfo,mt_teams_home_name,mt_teams_home_seed_seeding,'\
    'mt_teams_home_seed_type_short,mt_teams_away_name,mt_teams_away_seed_seeding,mt_teams_away_seed_type_short,'\
    'mt_status_name,mt_removed,mt_facts,mt_localderby,mt_hf,mt_periodlength,mt_numberofperiods,mt_overtimelength,'\
    'mt_bestofsets,mt_tobeannounced,islivescoringprovided)'\
    ' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,' \
        '?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
'''
