from misc import *
from nbastats import *
from calculatenba import *
import datetime
import heapq

NBA_YEAR = int(datetime.date.today().year)


def Create_NBA_Score(bet_dicts):

    top_3 = []
    low_3 = []

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

            nba_szn_stats = NBA_Season_Stats(player_name, str(NBA_YEAR))
            nba_recent_stats = Last_7_NBA_Events_Stats(player_name, str(NBA_YEAR))
            nba_against_team_stats = Last_5_NBA_Against_Team_Stats(player_name, NBA_YEAR, pp_abv_to_espn_abv[opp_team])

            szn_avg = Calc_Avg(nba_szn_stats, stat_type)
            recent_avg = Calc_Avg(nba_recent_stats, stat_type)
            team_avg = Calculate_Avg_Multiple_Years(nba_against_team_stats, stat_type)

            try:
                weighted_avg = ((.51*szn_avg) + (.41*recent_avg) + (.08*team_avg))
                stat_dif = float(stat_line) - float(weighted_avg)

                if len(top_3) < 3:
                    top_3.append((i, stat_dif))
                    top_3 = sorted(top_3, key=lambda x: x[1], reverse=True)

                elif stat_dif > top_3[2][1]:
                    top_3[2] = (i, stat_dif)
                    top_3 = sorted(top_3, key=lambda x: x[1], reverse=True)

                if len(low_3) < 3:
                    low_3.append((i, stat_dif))
                    low_3 = sorted(low_3, key=lambda x: x[1], reverse=False)

                elif stat_dif < low_3[2][1]:
                    low_3[2] = (i, stat_dif)
                    low_3 = sorted(low_3, key=lambda x: x[1], reverse=False)
                

            except TypeError:
                print('TypeError, NoneType for one of the averages (not enough data)')
                pass
            i += 1
            
            print('Continuing: ' + str(i) + '/' + str(len(bet_dicts)) + ' done.')

    best_under = {
        'Best_Under': bet_dicts[top_3[0][0]]['Player_Name'], 'Dif': top_3[0][1],
        '2nd_Best': bet_dicts[top_3[1][0]]['Player_Name'], '2nd_Dif': top_3[1][1],
        '3rd_Best': bet_dicts[top_3[2][0]]['Player_Name'], '3rd_Dif': top_3[2][1]
    }

    best_over = {
        'Best_Over': bet_dicts[low_3[0][0]]['Player_Name'], 'Dif': low_3[0][1],
        '2nd_Best': bet_dicts[low_3[1][0]]['Player_Name'], '2nd_Dif': low_3[1][1],
        '3rd_Best': bet_dicts[low_3[2][0]]['Player_Name'], '3rd_Dif': low_3[2][1]
    }
    
    return best_over, best_under