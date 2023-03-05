import json
from bs4 import BeautifulSoup

def NBA_Group_Len(JSON_Player_Object):
    """
    Gathers groups which represent Postseason and Regular Season
    Used to gather Tbls in each group
    Subtract 1 as we do not care about preseason
    """
    json_data = json.loads(JSON_Player_Object)
    groups = (json_data['page']['content']['player']['gmlog']['groups'])
    groups_len = (len(groups)) - 1

    if groups_len == 0:
        groups_len += 1
    
    return groups_len


def Gather_NBA_Tbls(JSON_Player_Object):
    """
    Game log stored into Tbls
    To iterate over all stats we will have to get a list of each tbls
    Each one represents a month in the game log
    Iterates over each group as well
    """
    
    json_data = json.loads(JSON_Player_Object)
    
    groups_len = NBA_Group_Len(JSON_Player_Object)
    
    
    tbls_list = []

    i = 0
    while i < groups_len:
        tbls = (json_data['page']['content']['player']['gmlog']['groups'][i]['tbls'])
        tbls_len = (len(tbls)-1)
        
        j = 0
        while j < tbls_len:
            tbls_list.append(json_data['page']['content']['player']['gmlog']['groups'][i]['tbls'][j])
            j += 1
            
        i += 1
    
    return tbls_list   