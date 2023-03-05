from dicts import *
from itertools import chain

def Calc_Season_Total(stats_list, stat_needed):
    """
    Iterates over stats list and calculates the 
    stat that is needed based on the key value matching
    Adds to total
    """
    
    season_stats = []
    
    for stat in stats_list:
        season_stats.append(stat[nba_stat_dict[stat_needed]])
    
    stat_sums = 0
    for i in season_stats:
        i = float(i)
        stat_sums = stat_sums + i
    
    
    return (stat_sums)


def Calc_Avg(stats_list, stat_needed):
    """
    Iterates over stats list and calculates the 
    stat that is needed based on the key value matching
    Divides by length of season_stats
    """
    total = Calc_Season_Total(stats_list, stat_needed)
    length = len(stats_list)

    return (total/length)


def Calculate_Avg_Multiple_Years(stats_list, stat_needed):

    season_stats = []

    for game in stats_list:
        season_stats.append(game[nba_stat_dict[stat_needed]])
            
    stat_sums = 0
    for stat in season_stats:
        stat = float(stat)
        stat_sums += stat
    
    try:
        avg = (stat_sums/len(season_stats))
        return avg
    except ZeroDivisionError:
        pass
    

