from misc import *
from nflstats import *
from calculatenfl import *
import datetime

NFL_YEAR = int(datetime.date.today().year) - 1


def Create_NFL_Score(bet_dicts):

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

            nfl_szn_stats = NFL_Season_Stats(player_name, str(NFL_YEAR))
            nfl_recent_stats = Last_4_NFL_Events_Stats(player_name, str(NFL_YEAR))
            nfl_against_team_stats = Last_2_NFL_Against_Team_Stats(player_name, NFL_YEAR, opp_team)

            szn_avg = Calc_Avg(nfl_szn_stats, nfl_stat_dict[position][stat_type])
            recent_avg = Calc_Avg(nfl_recent_stats, nfl_stat_dict[position][stat_type])
            team_avg = Calculate_Avg_Multiple_Years(nfl_against_team_stats, nfl_stat_dict[position][stat_type])
            
            try:
                weighted_avg = ((.4*szn_avg) + (.45*recent_avg) + (.15*team_avg))
                stat_dif = float(stat_line) - float(weighted_avg)

                if (stat_dif) < best_over['Dif']:
                    best_over = {'Player': player_name, 'Dif': stat_dif}

                if (stat_dif) > best_under['Dif']:
                    best_under = {'Player': player_name, 'Dif': stat_dif}
            except TypeError:
                print('No data, skipping')
                pass
            
            i += 1
            
            print('Continuing: ' + str(i) + '/' + str(len(bet_dicts)) + ' done.')


    return best_over, best_under