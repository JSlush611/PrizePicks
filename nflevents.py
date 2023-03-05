from parsenfl import *
from input import *
from createjson import *


def Gather_NFL_Events(JSON_Player_Object):
    """
    NFL gamelog can have multiple groups with post season
    However each group only has one tbls
    """
    
    json_data = json.loads(JSON_Player_Object)

    groups_len = NFL_Group_Len(JSON_Player_Object)

    events_list = []
    
    i = 0
    while i < groups_len:
        events_len = (len(json_data['page']['content']['player']['gmlog']['groups'][i]['tbls'][0]['events']))

        j = 0
        while j < events_len:
            events_list.append(json_data['page']['content']['player']['gmlog']['groups'][i]['tbls'][0]['events'][j])
            j += 1
        i += 1
        
    return events_list


def Gather_X_NFL_Events(JSON_Player_Object, num_of_games):
    """
    Gathers X amount of games for a player
    Checks if the first group avaible has enough games for the number
    If not, iterates over to next group collecting all games and moving to next
    Until the event list is equal to the num of games wanted
    """
    json_data = json.loads(JSON_Player_Object)

    group_path = json_data['page']['content']['player']['gmlog']['groups']
    
    events_list = []

    if len(group_path[0]['tbls'][0]['events']) > num_of_games:
        j = 0
        while j < num_of_games:
            events_list.append(group_path[0]['tbls'][0]['events'][j])
            j += 1
    else:
        games = 0
        i = 0
        while games < num_of_games:
            j = 0
            events_len = len(group_path[i]['tbls'][0]['events'])
            while j < events_len:
                events_list.append(group_path[i]['tbls'][0]['events'][j])
                games += 1
                j += 1

                if (games == num_of_games):
                    break
                
            i += 1

    return events_list

    
def Season_NFL_Events(full_name, year):
    """
    Gather all events from NFL Season
    Used in other functions
    """
    Player_Dict = get_Player_Info(full_name, 'nfl', year)

    JSON_Player_Object = Create_JSON_Object(Player_Dict)

    Events_List = Gather_NFL_Events(JSON_Player_Object)

    return Events_List