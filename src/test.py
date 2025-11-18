"""from systems.io_cli import afficher_choix_debase
afficher_choix_debase()





from systems.io_cli import afficher_stat_joueur, afficher_autreschoix
from data.statjoueur import  stat_joueur
afficher_stat_joueur(stat_joueur)
afficher_autreschoix()


from models.enemy import choisit_un_ennemi_random
print(choisit_un_ennemi_random()"""
stat = {
    "points de vie" : 100,
    "vie sociale" : 50,
    "points de connaissances" : 0,
    "multiplicateur de connaissances" : 1
}
action_choisie="Dormir"
from models.player import appliquer_chgt_stat_joueur
print(stat)
stat=appliquer_chgt_stat_joueur(stat,action_choisie)
print(stat)