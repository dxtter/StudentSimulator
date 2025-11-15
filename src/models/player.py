#Faire une un dictionnaire copie de data.statjoueur pour pas modifier la data principale
from data.statjoueur import stat_joueur
import copy 
def copie_stat_player() : 
    return copy.deepcopy (stat_joueur)

#modif les stats du joueur en fct de la cle de la tsat pas ex points de vie, cette fct permet de s'assurer que les stats ne dépassent pas  ou  0!
def modif_stat_joueur(stat_joueur, cle_stat, value):
    stat_joueur[cle_stat]+=value #prendre la valeur actuelle de la stat
    if cle_stat in ["vie sociale","points de connaissances"] : #verif de la stat modif si c est une de ces deux la
        stat_joueur[cle_stat]=max(0,min(100,stat_joueur[cle_stat])) #max(0,x), si la valeur stat est neg, elle est remise à 0. et la min choisit la plus petit des deux valeures en 0 et nouv valeur
    elif cle_stat=="points de vie" : 
        stat_joueur[cle_stat] = max(0,stat_joueur[cle_stat]) #permet de remettre a 0 pt de vie si c est negatif et de ne pas afficher en fin de partie des pt de vie negatif
    return stat_joueur