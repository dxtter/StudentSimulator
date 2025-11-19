#Faire une un dictionnaire copie de data.statjoueur pour pas modifier la data principale
from data.statjoueur import stat_joueur




import json
def modif_stat_joueur(stat_player,nom_action_choisie, ennemi_ou_skills,gagne_perdu= True): #donner comme arg dico stat player et str de l action choisie, ennemi_ou_skills c'est pour savoir dans quel fichier json aller chercher l'event qui change la stat , gagné ou perdu bool sert uniquement à savoir si on fait predre de la vie au joueur ou pas
    chemin_acces = "data/" + ennemi_ou_skills + ".json"
    
    with open (chemin_acces, encoding= "utf-8") as f :
        skills=json.load(f)
    
    for skill in skills :
        if nom_action_choisie== skill["nom"] : 
            break #pour arreter la boucle des que l action est trouvée dans le dic
    if gagne_perdu:
        if "sante_mentale" in skill: #cherche si sante_mentale est bien dans le dic action data 
            stat_player["vie sociale"]+=skill["sante_mentale"]
            stat_player["vie sociale"]= max(0,min(100,stat_player["vie sociale"])) #s'assure que la stat ne depasse pas 100 ou 0
        if "connaissance" in skill : #meme chose qu'avant 
            stat_player["points de connaissances"]+=skill["connaissance"]
            stat_player["points de connaissances"]= max(0,min(100,stat_player["points de connaissances"]))
    elif not gagne_perdu:
        if "punitivite" in skill : 
            stat_player["points de vie"]+=skill["punitivite"]

    return (stat_player) #return 




