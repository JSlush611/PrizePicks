from nbaevents import *
from itertools import chain


def Gather_NBA_Events_Stats(events_list):
    """
    Takes in event list and appends just the stats from the event object
    Iterates over every event in tbls appending all stats to stats_list
    Ignore All Star Game
    Ignore games where they play less than 3 minutes
    """
    
    stats_list = []

    i = 0
    while i < len(events_list):
        if 'Team' not in (events_list[i]['opp']['name']):
            if int(events_list[i]['stats'][0]) >= 3:
                stats_list.append(events_list[i]['stats'])
        i += 1
                       
    return stats_list


def NBA_Season_Stats(full_name, year):
    """
    Gather all stats from all games in NBA season
    for given player and year
    """

    events_list = Season_NBA_Events(full_name, year)

    stats_list = Gather_NBA_Events_Stats(events_list)

    return stats_list


def Gather_NBA_Teams_Stats(events_list, team):
    """
    Takes in event list and appends stats from team the user selects
    Team is three letter abbreviation, ATL etc
    Used in other function
    """
    
    stats_list = []

    for event in events_list:
        if (event['opp']['abbr']) == team:
            stats_list.append(event['stats'])
        
    return stats_list  



def Last_7_NBA_Events_Stats(full_name, year):
    """
    Gather last 7 NBA games from a player and their stats
    Used to get average of a players recent performances
    """
        
    Player_Dict = get_Player_Info(full_name, 'nba', year)
    
    JSON_Player_Object = Create_JSON_Object(Player_Dict)
    
    events_list = Gather_X_NBA_Events(JSON_Player_Object, 7)

    stats_list = Gather_NBA_Events_Stats(events_list)
    
    return stats_list


def Last_5_NBA_Against_Team_Stats(full_name, year, team):
    
    year = int(year)
    
    stats_list = []

    games = 0
    while games < 5:
        
        try:
            events_list = Season_NBA_Events(full_name, str(year))
            event_stats_verus_team = Gather_NBA_Teams_Stats(events_list, team)

            for game in event_stats_verus_team:
                if games < 5:
                    stats_list.append(game)
                    games += 1
                else:
                    break
                
            year = year - 1

        except KeyError:
            return (stats_list)
    
    return stats_list
