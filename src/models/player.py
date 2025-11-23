#Faire une un dictionnaire copie de data.statjoueur pour pas modifier la data principale

import json



def modif_stat_joueur(stat_player,nom_action_choisie, ennemi_ou_skills,multiplicateur_difficulte_globale,gagne_perdu= True): #donner comme arg dico stat player et str de l action choisie, ennemi_ou_skills c'est pour savoir dans quel fichier json aller chercher l'event qui change la stat , gagné ou perdu bool sert uniquement à savoir si on fait predre de la vie au joueur ou pas
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
            stat_player["points de connaissances"]+=skill["connaissance"]*stat_player["multiplicateur de connaissances"] #multiplie les pc ajoutés par le multiplicateur de connaissances
            stat_player["points de connaissances"]= max(0,min(100,stat_player["points de connaissances"]))
    elif not gagne_perdu:
        if "punitivite" in skill : 
            stat_player["points de vie"]+=skill["punitivite"]*multiplicateur_difficulte_globale #multiplie les pv enlevés par le multiplicateur de difficulté globale
            stat_player["points de vie"] = max(0, min(100, stat_player["points de vie"]))

    return (stat_player) #return 


def verif_sante_mentale_insuffisante(sante_mentale_actuelle) : #donner en argument un int de santé mentale actuelle du joueur
    if sante_mentale_actuelle <=20 :
        return True
    else :
        return False 
    #return bool pour savoir si la santé mentale est insuffisante(True) ou pas(False) (seuil à 20) 


def appliquer_choix_recompense(dico_recompense_choisie, dico_stats_joueur):

    

    for cle in dico_recompense_choisie:
        if cle == "sante_mentale":
            dico_stats_joueur["vie sociale"] += dico_recompense_choisie[cle]
            dico_stats_joueur["vie sociale"] = max(0, min(100, dico_stats_joueur["vie sociale"]))
        if cle == "points_de_vie":
            dico_stats_joueur["points de vie"] += dico_recompense_choisie[cle]
            dico_stats_joueur["points de vie"] = max(0, min(100, dico_stats_joueur["points de vie"]))
        if cle == "augmenter_multiplicateur_connaissances":
            dico_stats_joueur["multiplicateur de connaissances"] += dico_recompense_choisie[cle]
        if cle == "connaissance":
            dico_stats_joueur["points de connaissances"] += dico_recompense_choisie[cle]*dico_stats_joueur["multiplicateur de connaissances"] #multiplie les pc ajoutés par le multiplicateur de connaissances
            dico_stats_joueur["points de connaissances"] = max(0, min(100, dico_stats_joueur["points de connaissances"]))
        if cle == "multiplicateur_de_multiplicateur_de_connaissances":
            dico_stats_joueur["multiplicateur de connaissances"] *= dico_recompense_choisie[cle]
    return dico_stats_joueur
