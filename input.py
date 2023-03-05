from bs4 import BeautifulSoup
from misc import Cleanse_Link
import re
import requests

#Create requests Session Object to send requests
s = requests.Session()

#Update session objects with correct headers for requests
s.headers.update({
    'Host': 'www.espn.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
})

def Parse_ID(id_link):
    """Find players ID from their gamelog link which is built"""
    
    player_id = re.search(r"/id/(\d+)/", id_link).group(1)
        
    return player_id


def Parse_Name(id_link):
    """Find players name from their gamelog link which is built"""
    id_link = Cleanse_Link(id_link)

    player_name = re.search(r"([a-zA-Z]+(-[a-zA-Z]+)+)", id_link).group(1)

    return player_name


def Build_URL(player_id, mode, year):
    """
    Build the URL from the espn gamelog base
    Mode represents the sport they want NFL, NBA etc
    """

    player_url = 'https://www.espn.com/'+(mode)+'/player/gamelog/_/id/'+(player_id)+'/type/'+(mode)+'/year/'+(year)+''
    
    return player_url
    

  
def get_Player_Info(full_name, mode, year):
    """
    Creates URL to send get request to to recieve the results of a gamelog search
    Attempts to find a propery's content which contains the info we want
    If fails it means there is more then one player avaible to view their gamelog
    If this is the case it asks them which player they want and continues
    If no results it will return no results 
    """

    first_name, last_name = full_name.split(" ", 1)
    first_name = first_name.replace('.', '') #replace any . in name as it messes up comparison


    id_search_url = 'http://www.espn.com/'+(mode)+'/players/_/search/'+(last_name)

    id_search_html = s.get(id_search_url).content
    soup = BeautifulSoup(id_search_html, 'html.parser')

    try:
        id_link = soup.find('meta', property='og:url').attrs['content']
        
        #player_name = Parse_Name(id_link)
        player_id = Parse_ID(id_link)
        player_url = Build_URL(player_id, mode, year)
        
        return {'Player_Name': 'test','Player_ID': player_id}, player_url
    

    except AttributeError:

        check_for = 'http://www.espn.com/'+(mode)+'/player/_/id/'

        id_links = []

        for a_tag in soup.find_all('a'):
            link = a_tag.get('href')

            if check_for in link:
                id_links.append(link)
                
        if not id_links:
            return('No results, invalid search term')
        
        else:
            
            for i, link in enumerate(id_links, start=1):
                player_name = Parse_Name(link)
                current_first_name = (player_name.split("-")[0]).title()
                if current_first_name == first_name:
                    player_choice = i
                elif current_first_name.upper() == first_name: #check for two letter names, AJ etc
                    player_choice = i
                                
            player_id = Parse_ID(id_links[player_choice - 1])
            player_name = Parse_Name(id_links[player_choice - 1])
            player_url = Build_URL(player_id, mode, year)

            return {'Player_Name': player_name,'Player_ID': player_id}, player_url
