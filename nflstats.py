from nflevents import *

def Gather_NFL_Events_Stats(events_list):
    """
    Also takes in event list, only one tbls so does not
    need to iterate over tbls, just the list
    Ignore Pro bowl game
    """
    
    stats_list = []
    
    i = 0
    while i < len(events_list):
        if (events_list[i]['opp']['abbr'] != 'NFC') and (events_list[i]['opp']['abbr'] != 'AFC'):
            stats_list.append(events_list[i]['stats'])
                       
        i += 1
        
    return stats_list


def NFL_Season_Stats(full_name, year):
    """
    Gather all stats from all games in NFL season
    """

    events_list = Season_NFL_Events(full_name, year)

    stats_list = Gather_NFL_Events_Stats(events_list)

    return stats_list


def Gather_NFL_Team_Stats(events_list, team):
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



def Last_4_NFL_Events_Stats(full_name, year):
    
    Player_Dict = get_Player_Info(full_name, 'nfl', year)

    JSON_Player_Object = Create_JSON_Object(Player_Dict)

    events_list = Gather_X_NFL_Events(JSON_Player_Object, 4)

    stats_list = Gather_NFL_Events_Stats(events_list)

    return stats_list


def Last_2_NFL_Against_Team_Stats(full_name, year, team):
    """
    Get NFL games from a certain team for a player over 
    an amount of years
    """
    year = int(year)
    
    stats_list = []

    games = 0
    while games < 2:
        
        try:
            events_list = Season_NFL_Events(full_name, str(year))
            event_stats_verus_team = Gather_NFL_Team_Stats(events_list, team)

            for game in event_stats_verus_team:
                if games < 2:
                    stats_list.append(game)
                    games += 1
                else:
                    break
                
            year = year - 1

        except KeyError:
            return (stats_list)
    
    return stats_list