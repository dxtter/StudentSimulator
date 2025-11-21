from models.encounter import choixdispo
def afficher_choix_debase(): #fonction servant à afficher les choix de base à l'utilisateur
    print(f"Le premier choix est : {choixdispo()[0]}\nLe deuxième choix est : {choixdispo()[1]}\nLe troisième choix est : {choixdispo()[2]}")


def afficher_autreschoix(choixpossibles): #fonction servant à afficher les autres choix à l'utilisateur #j'ai modifié car sinon ça appelle la fonction autreschoix() et dcp c'est aléatoire à chaque fois
    
    print (f"1) {choixpossibles[0]}\n2) {choixpossibles[1]}\n3) {choixpossibles[2]}")


def afficher_stat_joueur(stat_joueur): #fonction servant à afficher les barres (stats principales du joueur)

    print("\nStatistiques actuelles de l'étudiant(e):\n")
    print (f"Points de vie :{stat_joueur['points de vie']}/100\n\nVie sociale :{stat_joueur['vie sociale']}/100\n\nPoints de connaissances :{stat_joueur['points de connaissances']}/100\n\nMultiplicateur de connaissances :{stat_joueur['multiplicateur de connaissances']}\n")
    #Daniel : j'ai ajouté le multiplicateur de connaissances 

def affichage_apres_epreuve(reussite):
    if reussite :
        print("bien joué ! Vous vous en êtes tirés pour cette fois mais l'année n'est pas encore finie Mouhahahaha")
    elif not reussite:
        print("Vous n'êtes qu'un bon à rien, revenez plus fort pour une prochaine épreuve, mais surveillez votre barre de vie SKIBIDI")