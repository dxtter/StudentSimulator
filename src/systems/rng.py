import random
import time
graine_actuelle = None # Variable stock la seed actuelle

def initialiser_rng(seed_entree=None): #configuration du seed aleatoire, si le joueur en fourni une, on prend la sienne, sinon on en cree une en fct de l'heure et de la date
    global graine_actuelle # On dit qu'on veut modifier la variable définie plus haut
    
    if seed_entree is not None and seed_entree != "": # cas ou le joueur donne une seed et le convertir en str pour eviter les bugs
        
        graine_actuelle = str(seed_entree)
    else: #autre cas 
        graine_actuelle = str(int(time.time())) 

    random.seed(graine_actuelle)
    
    
    return graine_actuelle

def calcul_chance_succes_epreuve(connaissance, difficulte, multiplicateur_global_diff): #donner un int connaissance à prendre sur la stat_player et la difficulté du boss à prendre dans dans le dico du boss choisi aléatoire)
    proba_reussite_epreuve =0.95* (connaissance/100)**(difficulte/3*multiplicateur_global_diff) #0.95 pour s'assurer que la proba ne soit jamais à 100
    return proba_reussite_epreuve

def reussite_ou_echec(proba_reussite):
    return random.random() <= proba_reussite

