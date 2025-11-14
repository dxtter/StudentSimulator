from models.encounter import choixdispo
def afficher_choix_debase():
    print(f"Le premier choix est : {choixdispo()[0]}\nLe deuxième choix est : {choixdispo()[1]}\nLe troisième choix est : {choixdispo()[2]}")

from models.encounter import autreschoix
def afficher_autreschoix():
    choixpossibles=autreschoix()
    print (f"1) {choixpossibles[0]}\n2) {choixpossibles[1]}\n3) {choixpossibles[2]}")


def afficher_stat_joueur(stat_joueur):

    print("\nStatistiques actuelles de l'étudiant(e):\n")
    print (f"Points de vie :{stat_joueur['points de vie']}/100\n\nVie sociale :{stat_joueur['vie sociale']}/100\n\nPoints de connaissances :{stat_joueur['points de connaissances']}/100\n")