

from models.encounter import trois_choix_recompense, choix_joueur_recompense,appliquer_choix_recompense,choix_joueur_récompense_inventaire
from systems.io_cli import afficher_recompenses_au_joueur, afficher_inventaire_du_joueur
stat_joueur = {
    "points de vie" : 80,
    "vie sociale" : 50,
    "points de connaissances" : 0,
    "multiplicateur de connaissances" : 1
}

inventiaire_joueur = {}
print(stat_joueur)
print(inventiaire_joueur)


liste_recompenses = trois_choix_recompense()
afficher_recompenses_au_joueur(liste_recompenses)
choix_recompense = choix_joueur_recompense(liste_recompenses)


effet_recompnes, nom_recompense = choix_recompense[0], choix_recompense[1]
if nom_recompense not in ["gagner un peu de vie", "augmenter le multiplicateur de connaissances globales"]:
    inventiaire_joueur[nom_recompense] = effet_recompnes
else : 
    appliquer_choix_recompense(effet_recompnes, stat_joueur)


print(stat_joueur)
print(inventiaire_joueur.keys())



choix_joueur_récompense_inventaire(inventiaire_joueur)