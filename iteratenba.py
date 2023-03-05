from nbastats import *
from calculatenba import *
from misc import Cleanse_Name
import datetime

NBA_YEAR = int(datetime.date.today().year)


def Compare_SZN_Avg_NBA(bet_dicts):

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

            nba_szn_stats = NBA_Season_Stats(player_name, str(NBA_YEAR))

            szn_avg = Calc_Avg(nba_szn_stats, stat_type)

            #print(player_name + (': ') + str(szn_avg))
            stat_dif = float(stat_line) - float(szn_avg)

            if (stat_dif) < best_over['Dif']:
                best_over = {'Player': player_name, 'Dif': stat_dif}

            if (stat_dif) > best_under['Dif']:
                best_under = {'Player': player_name, 'Dif': stat_dif}

            i += 1

    return best_over, best_under


def Compare_Recent_Avg_NBA(bet_dicts, type="recent"):

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

            nba_recent_stats = Last_7_NBA_Events_Stats(player_name, str(NBA_YEAR))

            recent_avg = Calc_Avg(nba_recent_stats, stat_type)
            #print(player_name + (': ') + str(recent_avg))

            stat_dif = float(stat_line) - float(recent_avg)

            if (stat_dif) < best_over['Dif']:
                best_over = {'Player': player_name, 'Dif': stat_dif}

            if (stat_dif) > best_under['Dif']:
                best_under = {'Player': player_name, 'Dif': stat_dif}

            i += 1

    return best_over, best_under


def Compare_Avg_Against_Team_NBA(bet_dicts):

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

            nba_against_team_stats = Last_5_NBA_Against_Team_Stats(player_name, NBA_YEAR, pp_abv_to_espn_abv[opp_team])
            
            game_length = len(nba_against_team_stats)

            if game_length < 5:
                print('Not full 5 games, averaging ' + str(game_length))

            against_team_avg = Calculate_Avg_Multiple_Years(nba_against_team_stats, stat_type)
            #print(player_name + ' ' + str(against_team_avg) + ' against: ' + pp_abv_to_espn_abv[opp_team])
            
            stat_dif = float(stat_line) - float(against_team_avg)

            if (stat_dif) < best_over['Dif']:
                best_over = {'Player': player_name, 'Dif': stat_dif}

            if (stat_dif) > best_under['Dif']:
                best_under = {'Player': player_name, 'Dif': stat_dif}

            i += 1

    return best_over, best_under