import random
import time


# Variable globale pour stocker la seed actuelle
# On la stocke pour pouvoir l'afficher au joueur (ex: "Seed de cette partie : 12345")
GRAINE_ACTUELLE = None

def initialiser_rng(seed_entree=None):

    """
    Configure le générateur aléatoire.
    - Si seed_entree est fourni (par le joueur), on l'utilise.
    - Sinon, on en crée une basée sur l'heure actuelle.
    """
    global GRAINE_ACTUELLE # On dit qu'on veut modifier la variable définie plus haut
    
    if seed_entree is not None and seed_entree != "":
        # Le joueur a donné une seed (ex: "CHIMIE_HARD")
        # On convertit tout en string pour éviter les bugs
        GRAINE_ACTUELLE = str(seed_entree)
    else:
        # Pas de seed donnée ? On en génère une aléatoire
        # On utilise l'heure exacte pour être sûr que c'est unique
        GRAINE_ACTUELLE = str(int(time.time()))
    
    # C'EST LA LIGNE MAGIQUE
    # Elle fige le destin de l'aléatoire pour tout le reste du programme
    random.seed(GRAINE_ACTUELLE)
    
    print(f"[DEBUG] Système RNG initialisé avec la graine : {GRAINE_ACTUELLE}")
    return GRAINE_ACTUELLE