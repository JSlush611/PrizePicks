from nflstats import *
from calculatenfl import *
from misc import Cleanse_Name
import datetime

NFL_YEAR = int(datetime.date.today().year) - 1

def Compare_SZN_Avg_NFL(bet_dicts):

    best_over = {'Player': 'default', 'Dif': 0}
    best_under = {'Player': 'default', 'Dif': 0}

    i = 0
    while i < len(bet_dicts):

        player_name = bet_dicts[i]['Player_Name']
        player_name = Cleanse_Name(player_name)

        if '+' in player_name:
            i += 1

        else:
            stat_type = bet_dicts[i]['Stat_Type']
            stat_line = bet_dicts[i]['Stat_Score']
            position = bet_dicts[i]['Position']

            nfl_szn_stats = NFL_Season_Stats(player_name, str(NFL_YEAR))

            szn_avg = Calc_Avg(nfl_szn_stats, nfl_stat_dict[position][stat_type])

            #print(''+ player_name + 'is a '+ (position) + ' and averaged: ' + str(szn_avg))
            stat_dif = float(stat_line) - float(szn_avg)

            if (stat_dif) < best_over['Dif']:
                best_over = {'Player': player_name, 'Dif': stat_dif}

            if (stat_dif) > best_under['Dif']:
                best_under = {'Player': player_name, 'Dif': stat_dif}

            i += 1

    return best_over, best_under


def Compare_Recent_Avg_NFL(bet_dicts):

    best_over = {'Player': 'default', 'Dif': 0}
    best_under = {'Player': 'default', 'Dif': 0}

    i = 0
    while i < len(bet_dicts):

        player_name = bet_dicts[i]['Player_Name']
        player_name = Cleanse_Name(player_name)
        position = bet_dicts[i]['Position']

        if '+' in player_name:
            i += 1

        else:
            stat_type = bet_dicts[i]['Stat_Type']
            stat_line = bet_dicts[i]['Stat_Score']

            nfl_recent_stats = Last_4_NFL_Events_Stats(player_name, str(NFL_YEAR))

            recent_avg = Calc_Avg(nfl_recent_stats, nfl_stat_dict[position][stat_type])
            #print(''+ player_name + 'is a '+ (position) + ' and averaged: ' + str(recent_avg))

            stat_dif = float(stat_line) - float(recent_avg)

            if (stat_dif) < best_over['Dif']:
                best_over = {'Player': player_name, 'Dif': stat_dif}

            if (stat_dif) > best_under['Dif']:
                best_under = {'Player': player_name, 'Dif': stat_dif}

            i += 1

    return best_over, best_under


def Compare_Avg_Against_Team_NFL(bet_dicts):

    best_over = {'Player': 'default', 'Dif': 0}
    best_under = {'Player': 'default', 'Dif': 0}

    i = 0
    while i < len(bet_dicts):

        player_name = bet_dicts[i]['Player_Name']
        player_name = Cleanse_Name(player_name)

        if '+' in player_name:
            i += 1

        else:
            stat_type = bet_dicts[i]['Stat_Type']
            stat_line = bet_dicts[i]['Stat_Score']
            opp_team = bet_dicts[i]['Team_Playing']
            position = bet_dicts[i]['Position']

            nfl_against_team_stats = Last_2_NFL_Against_Team_Stats(player_name, NFL_YEAR, opp_team)
            
            game_length = len(nfl_against_team_stats)

            if (game_length < 2) and (game_length != 0):
                print('Not full 2 games, averaging ' + str(game_length))

            against_team_avg = Calculate_Avg_Multiple_Years(nfl_against_team_stats, nfl_stat_dict[position][stat_type])

            if against_team_avg != None:
                #print(player_name + ' ' + str(against_team_avg) + ' against: ' + opp_team + '\n')
                
                stat_dif = float(stat_line) - float(against_team_avg)

                if (stat_dif) < best_over['Dif']:
                    best_over = {'Player': player_name, 'Dif': stat_dif}

                if (stat_dif) > best_under['Dif']:
                    best_under = {'Player': player_name, 'Dif': stat_dif}

            i += 1

    return best_over, best_under