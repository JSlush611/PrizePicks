import json

def Gather_Bets_Json():
    """
    Gather Bet data recieved from PrizePicks
    Turn into JSON
    """
    with open('bets.txt', 'r') as file:
        bets = file.readlines()
        
        bet_data = json.loads(bets[0])

    return bet_data


def Gather_Bets_From_Data(bet_data, Needed_Stat):
    """
    Gather all the bet objects and append to bets_list
    Gather all the players and append to players_list
    """
    bets_list = []
    players_list = []
    
    i = 0
    while i < (len(bet_data['data'])):

        stat_type = (bet_data['data'][i]['attributes']['stat_type'])
        
        if stat_type == Needed_Stat:
            stat_type = (bet_data['data'][i]['attributes']['stat_type'])

            bets_list.append(bet_data['data'][i])
        i += 1
        
    j = 0
    while j < (len(bet_data['included'])):
        if (bet_data['included'][j]['type'] == 'new_player'):
            players_list.append(bet_data['included'][j])
        j += 1
        
    return bets_list, players_list
    


def Create_Bet_Dicts(bets_list, players_list):
    """
    Players names were not matched to bets before, so use bets_list
    and players_list to create dictionary for each bet, with the players name
    the team they are playing, the stat line, the stat type, and the players id
    """
    
    new_bets = []

    i = 0
    while i < len(bets_list):
        id_needed = bets_list[i]['relationships']['new_player']['data']['id']

        j = 0

        while j < len(players_list):
            current_id = players_list[j]['id']
            if current_id == id_needed:
                new_bets.append({
                    "Stat_Score": bets_list[i]['attributes']['line_score'],
                    "Team_Playing": bets_list[i]['attributes']['description'],
                    "Stat_Type": bets_list[i]['attributes']['stat_type'],
                    "Player_ID": players_list[j]['id'],
                    "Player_Name": players_list[j]['attributes']['name'],
                    "Position": players_list[j]['attributes']['position']

                })
            j += 1
        i += 1
        
    return new_bets


def Create_Current_Bet_Dicts(Needed_Stat):
    bet_data = Gather_Bets_Json()
    bets_list, players_list = Gather_Bets_From_Data(bet_data, Needed_Stat)
    bet_dicts = Create_Bet_Dicts(bets_list, players_list)

    return bet_dicts

