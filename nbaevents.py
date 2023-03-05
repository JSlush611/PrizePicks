from parsenba import *
from input import *
from createjson import *

def Gather_All_NBA_Events(JSON_Player_Object):
    """
    Uses Gather_NBA_Tbls to collect every NBA Tbls
    Iterates each event from each Tbls and append them to events_list
    This will be all the players game, each game is stored as an event
    """
        
    tbls_list = Gather_NBA_Tbls(JSON_Player_Object)
    tbls_len = len(tbls_list)
    
    events_list = []
    
    i = 0
    while i < tbls_len:
        j = 0
        while j < len(tbls_list[i]['events']):
            events_list.append(tbls_list[i]['events'][j])
            j += 1
        i += 1
        
    return events_list


def Gather_X_NBA_Events(JSON_Player_Object, num_of_games):
    """
    Gathers X amount of games for a player
    Checks if the first tbls avaible has enough games for the number
    If not, iterates over each table collecting all games and moving to next
    Until the event list is equal to the num of games wanted
    """

    tbls_list = Gather_NBA_Tbls(JSON_Player_Object)
    
    events_list = []

    if len(tbls_list[0]['events']) > num_of_games:
        j = 0
        while j < num_of_games:
            events_list.append(tbls_list[0]['events'][j])
            j += 1
    else:
        games = 0
        i = 0
        while games < num_of_games:
            j = 0
            events_len = len(tbls_list[i]['events'])
            while j < events_len:
                events_list.append(tbls_list[i]['events'][j])
                games += 1
                j += 1

                if (games == num_of_games):
                    break
                
            i += 1

    return events_list

    
def Season_NBA_Events(full_name, year):
    """
    Gather all events from NBA season
    Used in other functions
    """
        
    Player_Dict = get_Player_Info(full_name, 'nba', year)
    
    JSON_Player_Object = Create_JSON_Object(Player_Dict)
    
    events_list = Gather_All_NBA_Events(JSON_Player_Object)
    
    return events_list



