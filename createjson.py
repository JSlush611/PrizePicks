import json
from bs4 import BeautifulSoup
import requests


#Create requests Session Object to send requests
s = requests.Session()

#Update session objects with correct headers for requests
s.headers.update({
    'Host': 'www.espn.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
})


def Create_JSON_Object(Player_Dict):
    """
    Create valid JSON Object to parse from the results of a get request
    to the players gamelog which is stored in Player_Dict
    Will be used for all the parsing
    """
    
    Player_Stats_HTML = s.get(Player_Dict[1])

    soup = BeautifulSoup(Player_Stats_HTML.content, 'html.parser')
    body = soup.body
    JSON_Player_String = body.find('script', type='text/javascript').string
    JSON_Player_Object = JSON_Player_String[JSON_Player_String.index('=')+1:][:-1]
    
    return JSON_Player_Object
 
   



