from random import randint

def choixdispo ():
    return ['dormir','étudier','autres']
import json


def autreschoix():
    with open ("src\data/skills.json", encoding= "utf-8") as f :
        skills=json.load(f)
    autres =[]
    for i in skills:
        if i["nom"]!='dormir' and i["nom"]!="étudier":
            autres.append(i["nom"])
    nouvelles_actions = []
    while len(nouvelles_actions)<3:
        i = randint(0,len(autres)-1)
        if autres[i] not in nouvelles_actions:
            nouvelles_actions.append(autres[i])
   )


    return  nouvelles_actions



