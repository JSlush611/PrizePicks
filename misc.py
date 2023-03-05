def Cleanse_Name(player_name):
    """
    Replace any names with ' in them as it messes 
    up the request and search
    """
    player_name = player_name.strip()
    player_name = player_name.replace("'", "")
    player_name = player_name.title()
    
    return player_name


def Cleanse_Link(id_link):
    """
    Remove any periods in the name in the link to parse their name out
    Only removes periods in the name part of the link
    """
    link_start = id_link[:36]
    link_end = id_link[36:]
    link_end = link_end.replace(".","")
    cleansed_link = link_start + link_end

    return cleansed_link