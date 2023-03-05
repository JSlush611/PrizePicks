import json
from bs4 import BeautifulSoup


def NFL_Group_Len(JSON_Player_Object):
    """
    Gather groups incase of post season 
    """
    json_data = json.loads(JSON_Player_Object)
    groups = (json_data['page']['content']['player']['gmlog']['groups'])
    groups_len = (len(groups)) 
    
    return groups_len

