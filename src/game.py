from systems.io_cli import afficher_choix_debase
afficher_choix_debase()

from systems.rng import initialiser_rng

from data.statjoueur import stat_joueur
import copy #copie du dico des stats du joueur pour pouvoir le modif

def main():
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
    while stat_joueur["points de vie"] > 0 and compteur_de_tours <=1000:  #boucle principale tant que la vie du joueur est supérieure à 0,jeu continue
        compteur_de_tours += 1
        for tour in range(1,6):
            print(f"Tour de préparation {tour}/5") #afficher le nbr de tour de preparation 
            








if __name__ == "__main__":
    main()
