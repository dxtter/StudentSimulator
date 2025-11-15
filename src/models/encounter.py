from random import randint

def choixdispo ():  #fonction renvoyant une liste des choix de base de l'utilisateur à chaque tour de préparation
    return ['Dormir','Etudier','Autres']

import json


def autreschoix(): #fonction qui renvoie une liste des nouvelles actions, actions qui seront affichées si l'utilisateur séléctionne le choix 'Autres' dans les choix de base 
    with open ("data/skills.json", encoding= "utf-8") as f :
        skills=json.load(f)
    autres =[]
    for i in skills:
        if i["nom"]!='Dormir' and i["nom"]!="Etudier":
            autres.append(i["nom"])
    nouvelles_actions = []
    while len(nouvelles_actions)<3:
        i = randint(0,len(autres)-1)
        if autres[i] not in nouvelles_actions:
            nouvelles_actions.append(autres[i])
   


    return  nouvelles_actions

def action_choisie(choix_utilisateur,liste_choix): #il faut donner à la fonction l'input de l'utilisateur et la liste des choix possibles (soit les choix de base soit les autres choix)

    if choix_utilisateur == '1':
        return liste_choix[0]
    elif choix_utilisateur == '2':
        return liste_choix[1]
    elif choix_utilisateur == '3' :
        return liste_choix[2]
    else:
        return 'Choix invalide'  #gestion d'erreur si l'utilisateur entre un choix invalide


