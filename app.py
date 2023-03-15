from parsebets import *
from iteratenba import *
from iteratenfl import *
from createnbascore import *
from createnflscore import *

bet_dicts = Create_Current_Bet_Dicts('Rebounds')

nba = Create_NBA_Score(bet_dicts)
print(nba)

#test = Create_NBA_Score(bet_dicts)
#print(test)


