#Faire une un dictionnaire copie de data.statjoueur pour pas modifier la data principale
from data.statjoueur import stat_joueur
import copy 
def copie_stat_player() : 
    return copy.deepcopy (stat_joueur)

