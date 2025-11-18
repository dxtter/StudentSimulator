#Faire une un dictionnaire copie de data.statjoueur pour pas modifier la data principale
from data.statjoueur import stat_joueur

#modif les stats du joueur en fct de la cle de la tsat pas ex points de vie, cette fct permet de s'assurer que les stats ne dépassent pas  ou  0!
def modif_stat_joueur(stat_joueur, cle_stat, value): #value est la la valeur de modification que va subir stat_joueur[cle_stat] : ex : l'examen fait perdre 10 points de vie alors stat_joueur["points de vie"] += -10 
    stat_joueur[cle_stat]+=value #prendre la valeur actuelle de la stat
    if cle_stat in ["vie sociale","points de connaissances"] : #verif de la stat modif si c est une de ces deux la
        stat_joueur[cle_stat]=max(0,min(100,stat_joueur[cle_stat])) #max(0,x), si la valeur stat est neg, elle est remise à 0. et la min choisit la plus petit des deux valeures en 0 et nouv valeur
    elif cle_stat=="points de vie" : 
        stat_joueur[cle_stat] = max(0,stat_joueur[cle_stat]) #permet de remettre a 0 pt de vie si c est negatif et de ne pas afficher en fin de partie des pt de vie negatif
    return stat_joueur


import json
def appliquer_chgt_stat_joueur(stat_player,nom_action_choisie) :#ennemi_ou_skills donner comme arg dico stat player et str de l action choisie
   # chemin_acces = "data/" + ennemi_ou_skills + ".json"
    
    with open ("data/skills.json", encoding= "utf-8") as f :
        skills=json.load(f)
    action_data=""
    for skill in skills :
        if nom_action_choisie== skill["nom"] : 
            action_data= skill 
            break #pour arreter la boucle des que l action est trouvée dans le dic
    if "sante_mentale" in action_data: #cherche si sante_mentale est bien dans le dic action data 
        stat_player["vie sociale"]+=skill["sante_mentale"]
    if "connaissances" in action_data : #meme chose qu'avant 
        stat_player["points de connaissances"]+=skill["connaissance"]
    return (stat_player) #return 

