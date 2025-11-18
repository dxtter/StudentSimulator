

from systems.rng import initialiser_rng
from models.encounter import action_choisie, choixdispo, autreschoix

from data.statjoueur import stat_joueur 
from systems.io_cli import afficher_stat_joueur, afficher_choix_debase,  afficher_autreschoix
import copy #copie du dico des stats du joueur pour pouvoir le modif



def main():

    stat_player = copy.deepcopy(stat_joueur)  #copie du dico des stats du joueur pour pouvoir le modif sans toucher à l'original !!!!! utilisation de celui-là uniquement, jamais stat_joueur directement !!!!!
    print("BIENVENUE A L'UNIVERSITE")
    
    # 1. Demander au joueur s'il a une seed (facultatif)
    choix_seed = input("Entrez une graine (ou Entrée pour aléatoire) : ")
    
    # 2. Initialiser le destin
    seed_utilisee = initialiser_rng(choix_seed)
    
    print(f"Partie lancée ! Seed : {seed_utilisee}")
    print("(Notez ce code pour rejouer exactement la même partie !)")
    
    # ... Le reste du jeu commence ici ...
    # ... Création du joueur ...
    compteur_de_tours = 0 
    # ... Boucle de jeu ...
    while stat_joueur["points de vie"] > 0 and compteur_de_tours <=0:  #boucle principale tant que la vie du joueur est supérieure à 0,jeu continue
        compteur_de_tours += 1
        for tour in range(1,2): #modifié pour faire 1 seul tour de préparation pour l'instant
            print(f"Tour de préparation {tour}/5") #afficher le nbr de tour de preparation 
            afficher_stat_joueur(stat_player)  #afficher les stats du joueur
            afficher_choix_debase()  #afficher les choix de base 
            liste_a_disposition_du_joueur= choixdispo() 
            #gérer choix de l'utilisateur
            
            v_action_choisie = action_choisie(liste_a_disposition_du_joueur)   
            print(f"l'utilisateur a choisi : {v_action_choisie}")
            if v_action_choisie == 'Autres':
                
                liste_a_disposition_du_joueur= autreschoix()
                afficher_autreschoix(liste_a_disposition_du_joueur)
                v_action_choisie= action_choisie(liste_a_disposition_du_joueur)
                print(f"L'utilisateur a choisi : {v_action_choisie}")


            








if __name__ == "__main__":
    main()
