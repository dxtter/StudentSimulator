from systems.io_cli import afficher_choix_debase
afficher_choix_debase()





from systems.io_cli import afficher_stat_joueur, afficher_autreschoix
from data.statjoueur import  stat_joueur
afficher_stat_joueur(stat_joueur)
afficher_autreschoix()


from models.enemy import choisit_un_ennemi_random
print(choisit_un_ennemi_random())