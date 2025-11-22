from random import randint
from models.player import verif_sante_mentale_insuffisante
from copy import deepcopy

def choixdispo ():  #fonction renvoyant une liste des choix de base de l'utilisateur à chaque tour de préparation
    return ['Dormir','Etudier','Autres']

import json


def autreschoix(SM_insuffisante): 
    with open ("data/skills.json", encoding= "utf-8") as f :
        liste_skills_json = json.load(f)
        skills_json =deepcopy(liste_skills_json)
    nouveaux_skills={}
    liste_interdits = ["Dormir","Etudier"]
    while len(nouveaux_skills) <= 1:
        indice_element_json = randint(0, len(skills_json)-1)

        cle_nom=liste_skills_json[indice_element_json].get("nom") #renvoie la valeur de la cle nom 
        if cle_nom not in liste_interdits :
            liste_interdits.append(cle_nom)
            skills_json[indice_element_json].pop("nom")
            nouveaux_skills[cle_nom]=skills_json[indice_element_json]
    
    while len(nouveaux_skills) <= 2:
        indice_element_json = randint(0, len(skills_json)-1)
        cle_nom=liste_skills_json[indice_element_json].get("nom") #renvoie la valeur de la cle nom
        if SM_insuffisante:
            
            if cle_nom not in liste_interdits and skills_json[indice_element_json]["sante_mentale"] >0:
                nouveaux_skills[cle_nom] = skills_json[indice_element_json]
        else :
            if cle_nom not in liste_interdits:
                skills_json[indice_element_json].pop("nom")
                nouveaux_skills[cle_nom]= skills_json[indice_element_json]
    liste_cles_dico = list(nouveaux_skills.keys())
    return liste_cles_dico





    
    
    
    




def action_choisie(liste_choix): #il faut donner à la fonction l'input de l'utilisateur et la liste des choix possibles (soit les choix de base soit les autres choix)
    choix_utilisateur =0
    while choix_utilisateur not in [1,2,3]:
        choix_utilisateur = input("Choisissez une action (1, 2, ou 3) : ")
        if choix_utilisateur == '1':
            return liste_choix[0]
        elif choix_utilisateur == '2':
            return liste_choix[1]
        elif choix_utilisateur == '3' :
            return liste_choix[2]
        else : 
            print("veuillez choisir un nombre entre 1 et 3")
    
    
def verif_choix_valide_cas_sante_mentale(choix_utilisateur): #fonction servant à vérifier si le choix de l'utilisateur est valide dans le cas où sa santé mentale est insuffisante
    with open ("data/skills.json", encoding= "utf-8") as f :
        skills=json.load(f)
    for skill in skills:
        if skill["nom"]==choix_utilisateur:
            
            if skill["sante_mentale"]>0:
                return True #renvoie True si le choix est valide (ajoute de la santé mentale)
            else :
                return False #renvoie False si le choix n'est pas valide (n'ajoute pas de santé mentale)
            
def trois_choix_recompense():
    
    gagner_un_peu_de_vie =  {
    "sante_mentale" : 0,
    "points_de_vie": 5,
    "connaissance": 0,
    "augmenter_multiplicateur_connaissances" : 0,
    "multiplicateur_de_multiplicateur_de_connaissances" : 1,
    "nb_tours_d'application" : 0
}
    augmenter_multiplicateur =  {
    "sante_mentale" : 0,
    "points_de_vie": 0,
    "connaissance": 0,
    "augmenter_multiplicateur_connaissances" : 0.1,
    "multiplicateur_de_multiplicateur_de_connaissances" : 1,
    "nb_tours_d'application" : 0
}

    
    dico_recompenses = {"gagner un peu de vie" : gagner_un_peu_de_vie,
                        "augmenter le multiplicateur de connaissances globales" : augmenter_multiplicateur
                        }
    with open("data/items.json", encoding= "utf_8" ) as f :
        items = json.load(f)
    indice_element_item = randint(0, len(items)-1)
    nom_objet =items[indice_element_item].pop("nom")
    
    dico_recompenses[nom_objet] = items[indice_element_item]

    return dico_recompenses #renvoie un dictionnaire avec 3 choix de récompenses possibles (2 de fixes et 1 aléatoire parmi items.json)
    
def choix_joueur_recompense(dico_reco): 
    while True:
        choix_utilisateur = input("Entrez le numéro de votre choix : ")
        if choix_utilisateur in ['1', '2', '3']:
            liste_cles = list(dico_reco.keys())
            nom_recompense_choisie = liste_cles[int(choix_utilisateur)-1]
            print(f"Vous avez choisi : {nom_recompense_choisie}")
            
            return dico_reco.pop(nom_recompense_choisie), nom_recompense_choisie #renvoie le dico avec les effets de la récompense choisie et son nom 
        
        else:
            print("Choix invalide. Veuillez choixir un numéro entre 1 et 3.")
            

    
def appliquer_choix_recompense(dico_recompense_choisie, dico_stats_joueur):

    

    for cle in dico_recompense_choisie:
        if cle == "sante_mentale":
            dico_stats_joueur["vie sociale"] += dico_recompense_choisie[cle]
            dico_stats_joueur["vie sociale"] = max(0, min(100, dico_stats_joueur["vie sociale"]))
        elif cle == "points_de_vie":
            dico_stats_joueur["points de vie"] += dico_recompense_choisie[cle]
            dico_stats_joueur["points de vie"] = max(0, min(100, dico_stats_joueur["points de vie"]))
        elif cle == "connaissance":
            dico_stats_joueur["points de connaissances"] += dico_recompense_choisie[cle]
            dico_stats_joueur["points de connaissances"] = max(0, min(100, dico_stats_joueur["points de connaissances"]))
        elif cle == "augmenter_multiplicateur_connaissances":
            dico_stats_joueur["multiplicateur de connaissances"] += dico_recompense_choisie[cle]
        elif cle == "multiplicateur_de_multiplicateur_de_connaissances":
            dico_stats_joueur["multiplicateur de connaissances"] *= dico_recompense_choisie[cle]

    

            



