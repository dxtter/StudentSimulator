from systems.io_cli import afficher_choix_debase
afficher_choix_debase()

from systems.rng import initialiser_rng

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
    # ... Boucle de jeu ...










if __name__ == "__main__":
    main()
