from random import randint
import json
def choisit_un_ennemi_random(): #return le nom de l'ennemi aléatoire choisi

    with open("data/enemies.json", encoding= 'utf-8') as f:
        data_enemies = json.load(f)
        nom_ennemi_aleatoire_choisi = data_enemies[randint(0,len(data_enemies)-1)]["nom"]
    return nom_ennemi_aleatoire_choisi

