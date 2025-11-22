

from systems.rng import initialiser_rng, calcul_chance_succes_epreuve, reussite_ou_echec
from systems.io_cli import afficher_stat_joueur, afficher_choix_debase,  afficher_autreschoix, affichage_apres_epreuve, afficher_recompenses_au_joueur, afficher_inventaire_du_joueur,inventaire_ou_non

from models.encounter import action_choisie, choixdispo, autreschoix,verif_choix_valide_cas_sante_mentale, trois_choix_recompense,choix_joueur_recompense, choix_joueur_objet_inventaire
from models.player import modif_stat_joueur, verif_sante_mentale_insuffisante, appliquer_choix_recompense
from models.enemy import choisit_un_ennemi_random

from data.statjoueur import stat_joueur 
import json

import copy #copie du dico des stats du joueur pour pouvoir le modif



def main():

    stat_player = copy.deepcopy(stat_joueur)  #copie du dico des stats du joueur pour pouvoir le modif sans toucher à l'original !!!!! utilisation de celui-là uniquement, jamais stat_joueur directement !!!!!
    BOLD = '\033[1m'
    RESET = '\033[0m'
    RESET = "\033[0m"
    VERT= "\033[32m"
    ROUGE = "\033[31m"
    print(f"""{BOLD}
    #######################################################
                    BIENVENUE À L'UNIVERSITÉ
    #######################################################{RESET}
        
Bienvenue, étudiant(e) courageux(se), dans l'arène académique la plus 
impitoyable de la région. Votre objectif est simple : survivre aux sessions 
intenses de révisions, aux assauts sournois de la fatigue mentale,afin de progresser de salle en salle.
Chaque épreuve sera précédée d'une session de 5 tours de préparation. Lors de ces  tours, choisissez judicieusement vos actions :

- {BOLD}Dormir{RESET} vous permettra de retrouver de l'équilibre mental.

- {BOLD}Étudier{RESET} fera grimper votre barre de connaissances (⚠️ si vous êtes en forme uniquement !).

- Tentez d'{BOLD}Autres{RESET} actions risquées pour des effets inattendus !


Votre périple commence maintenant. Votre Santé Mentale est votre ressource la plus précieuse, si vous passez en dessous de la barre des 20, vous ne pourrez plus acquérir de la connaissance. Gérez la donc bien !""")
        
        # 1. Demander au joueur s'il a une seed (facultatif)
    choix_seed = input("Entrez une graine (ou Entrée pour aléatoire) : ")
        
        # 2. Initialiser le destin
    seed_utilisee = initialiser_rng(choix_seed)
        
    print(f"Partie lancée ! Seed : {seed_utilisee}")
    print("(Notez ce code pour rejouer exactement la même partie !)\n")
        
        # ... Le reste du jeu commence ici ...
        # ... Création du joueur ...
    compteur_de_tours_globaux = 0 
    multiplicateur_global_difficulte = 0.95  #multiplicateur global de difficulté qui augmente légèrement à chaque tour global
    inventaire_joueur = {}  #dictionnaire de l'inventaire du joueur, vide au début
    copie_ancienne_stat_player = copy.deepcopy(stat_player)  #copie des stats du joueur pour afficher les changements de stats après chaque modification
        # ... Boucle de jeu ...
    while stat_player["points de vie"] > 0 and compteur_de_tours_globaux <=100:  #boucle principale tant que la vie du joueur est supérieure à 0,jeu continue
        compteur_de_tours_globaux += 1
        multiplicateur_global_difficulte += 0.05  #augmente légèrement la difficulté globale à chaque tour
        stat_player["points de connaissances"] =0 #à chaque tour, le joueur gagne des points de connaissance en fonction de son multiplicateur
        ennemi = choisit_un_ennemi_random() #choisir un ennemi aléatoire (son nom)
        print(f"\nVous allez affronter : {ennemi} après les 5 tours de préparation ! Bonne chance !")
        with open("data/enemies.json", encoding="utf-8") as f: #ouvre le fichier json avec tous les ennemis
            ennemis = json.load(f)
            for e in ennemis:
                if e["nom"] == ennemi:
                    ennemi = e #trouve le dico de l'ennemi choisi !!! ennemi devinent un dictionnaire et non une chaine de caractere
                    break
        print(f"Sa difficulté est de : {ennemi['difficulte']*multiplicateur_global_difficulte} \n ") #affiche la difficulté de l'ennemi multipliée par le multiplicateur global de difficulté
        bool_consult_inventaire = inventaire_ou_non()  #demande au joueur s'il veut consulter son inventaire
        if bool_consult_inventaire:
            afficher_inventaire_du_joueur(inventaire_joueur)  #affiche l'inventaire du joueur s'il le souhaite
            choix_objet_inventaire = choix_joueur_objet_inventaire(inventaire_joueur)
            if choix_objet_inventaire is not None:
                copie_ancienne_stat_player = copy.deepcopy(stat_player)  #met à jour la copie des stats du joueur avant modification
                stat_player= appliquer_choix_recompense(choix_objet_inventaire[0], stat_player)  #applique les effets de l'objet choisi sur les stats du joueur [0] car c'est les effets qui sont à l'index 0 du tuple renvoyé
                print(f"Vous avez utilisé {choix_objet_inventaire[1]} avant l'épreuve.")  #[1] car c'est le nom de l'objet qui est à l'index 1 du tuple renvoyé
                #ne pas oublier de faire une fonction qui affiche les changments de stat
                afficher_stat_joueur(stat_player, copie_ancienne_stat_player)  #affiche les stats du joueur après l'utilisation de l'objet 



        for tour_preparation in range(1,7): #modifié pour faire 5 tours de préparation pour l'instant + 1 tour combat de boss (tour 6)
            sante_mentale_insuffisante = verif_sante_mentale_insuffisante(stat_player["vie sociale"]) #vérifie à chaque tour de préparation si la santé mentale du joueur est insuffisante (True ou False)
            afficher_stat_joueur(stat_player, copie_ancienne_stat_player)  #afficher les stats du joueur
            
            if tour_preparation == 6: #tour du combat de boss
                print(f"{ROUGE}----- TOUR DE COMBAT DE BOSS -----{RESET}") #print tour de combat de boss si c'est le tour 6
                print("Tic Tac... L'heure a sonné... La deadline est terminée.. J'espère que vous êtes bien préparé(e)\n")
                
                proba_reussite = calcul_chance_succes_epreuve(stat_player["points de connaissances"], ennemi["difficulte"], multiplicateur_global_difficulte) #calcule la proba de reussite de l'epreuve en fonction de la connaissance du joueur et de la difficulté de l'ennemi, la multipli global est déjà pris en compte
                print(f"[DEBUG] Probabilité de réussite de l'épreuve : {proba_reussite}")
                reussite = reussite_ou_echec(proba_reussite) #détermine si le joueur réussit ou échoue l'épreuve en fonction de la proba calculée avec le module random (seedé ou pas)
                affichage_apres_epreuve(reussite) #affiche un message en fonction de la réussite ou de l'échec
                copie_ancienne_stat_player = copy.deepcopy(stat_player)  #met à jour la copie des stats du joueur avant modification
                stat_player= modif_stat_joueur(stat_player, ennemi["nom"], "enemies",multiplicateur_global_difficulte , reussite) #modifie les stats du joueur en fonction de la réussite ou de l'échec de l'épreuve contre l'ennemi
                
                print(f"[DEBUG]{stat_player}")
                if reussite:
                    dico_reco = trois_choix_recompense() #génère un dictionnaire avec 3 choix de récompenses possibles
                    afficher_recompenses_au_joueur(dico_reco) #affiche les choix de récompenses au joueur
                    stat_recompense_choisie, nom_recompense_choisie = choix_joueur_recompense(dico_reco) #demande au joueur de choisir une récompense et renvoie le dico des effets de la récompense choisie et son nom
                    print(f"[DEBUG] Récompense choisie : {nom_recompense_choisie} avec effets {stat_recompense_choisie}")
                    copie_ancienne_stat_player = copy.deepcopy(stat_player)  #met à jour la copie des stats du joueur avant modification
                    if nom_recompense_choisie not in ["gagner un peu de vie", "augmenter le multiplicateur de connaissances globales"]:
                        inventaire_joueur[nom_recompense_choisie] = stat_recompense_choisie #ajoute l'objet choisi dans l'inventaire du joueur s'il ne s'agit pas d'une des 2 récompenses fixes
                        print(f"Vous avez ajouté {nom_recompense_choisie} à votre inventaire.")
                    else : 
                        print(f"Vous avez choisi la récompense : {nom_recompense_choisie}.")
                        stat_player= appliquer_choix_recompense(stat_recompense_choisie, stat_player)#applique les effets de la récompense choisie sur les stats du joueur
                        print(f"[DEBUG] Statistiques du joueur après application de la récompense : {stat_player}")
                    afficher_inventaire_du_joueur(inventaire_joueur) #affiche l'inventaire du joueur après l'ajout éventuel d'un objet

                break  #sortir de la boucle de préparation pour revenir à la boucle principale car fin des tours de préparation

                
                
            else:
                print(f"Tour de préparation {tour_preparation}/5") #afficher le nbr de tour de preparation 
            
                choix_valide_final = False 
                liste_a_disposition_du_joueur= choixdispo()
                while not choix_valide_final:
                    afficher_autreschoix(liste_a_disposition_du_joueur)

                    v_action_choisie = action_choisie(liste_a_disposition_du_joueur)

                    if v_action_choisie == 'Autres':
                        liste_a_disposition_du_joueur= autreschoix(sante_mentale_insuffisante)
                        afficher_autreschoix(liste_a_disposition_du_joueur)
                        v_action_choisie= action_choisie(liste_a_disposition_du_joueur)
                        if sante_mentale_insuffisante:
                            if verif_choix_valide_cas_sante_mentale(v_action_choisie):
                                choix_valide_final = True
                            else:
                                print(f"{ROUGE} Veuillez choisir une action qui vous permettra de regagner de la santé mentale car votre santé mentale est trop basse.{RESET}")
                        else:
                            choix_valide_final = True
                    else:
                        if sante_mentale_insuffisante:
                            if verif_choix_valide_cas_sante_mentale(v_action_choisie):
                                choix_valide_final = True
                            else:
                                print(f"{ROUGE}Votre santé mentale est trop basse pour cette action, veuillez en choisir une autre qui vous permettra de regagner de la santé mentale.{RESET}")
                        else:
                            choix_valide_final = True    

                            #ici modfication de la stat de la stat du joueur en fonction de l'action choisie
            copie_ancienne_stat_player = copy.deepcopy(stat_player)  #met à jour la copie des stats du joueur avant modification
            stat_player = modif_stat_joueur(stat_player,v_action_choisie,"skills",multiplicateur_global_difficulte) #modifie les stats du joueur en fonction de l'action choisie et du multiplicateur de difficulté globale
                        
    


            








if __name__ == "__main__":
    main()




