from random import randint

def choixdispo ():
    return ['Dormir','Etudier','Autres']

import json


def autreschoix():
    with open ("../../data/skills.json", encoding= "utf-8") as f :
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



