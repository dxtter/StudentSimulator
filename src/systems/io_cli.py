from models.encounter import choixdispo
RESET = "\033[0m" #pour les couleurs 
VERT= "\033[32m"
ROUGE = "\033[31m"
BLEU = "\033[34m"
BLEU_VIF = "\033[34;1m"
VERT_VIF  = "\033[92;1m"
MAUVE = "\033[35m"
JAUNE = "\033[33m"

def afficher_choix_debase(): #fonction servant à afficher les choix de base à l'utilisateur
    print(f"Le premier choix est : {choixdispo()[0]}\nLe deuxième choix est : {choixdispo()[1]}\nLe troisième choix est : {choixdispo()[2]}")


def afficher_autreschoix(choixpossibles): #fonction servant à afficher les autres choix à l'utilisateur #j'ai modifié car sinon ça appelle la fonction autreschoix() et dcp c'est aléatoire à chaque fois
    
    print (f"1) {choixpossibles[0]}\n2) {choixpossibles[1]}\n3) {choixpossibles[2]}")

def affichage_apres_epreuve(reussite,nom_ennemi): #fonction servant à afficher un message en fonction de la réussite ou de l'échec de l'épreuve, donner un bool reussite (True si reussite, False si echec) et le nom de l'ennemi affronté
    if reussite :
        print(f"{VERT}Bien joué ! Vous vous en êtes tirés pour cette fois mais l'année n'est pas encore finie Mouhahahaha{RESET}")
        print(f"{VERT}Vous avez roulé sur {nom_ennemi}! Félicitations !{RESET}")
    elif not reussite:
        print(f"{ROUGE}Vous n'êtes qu'un bon à rien, revenez plus fort pour une prochaine épreuve, mais surveillez votre barre de vie SKIBIDI{RESET}")
        print(f"{ROUGE}{nom_ennemi} vous a roulé dessus!{RESET}")


def afficher_recompenses_au_joueur(dico_reco):
    print("Voici les récompenses parmi lesquelles vous pouvez choisir :")
    for i, cle in enumerate(dico_reco.keys(), start=1):
        print(f"{i}) {cle}")

def afficher_inventaire_du_joueur(inventaire_joueur): #donner un dico d'inventaire, oui_ou_non bool pour savoir si on affiche l'inventaire ou pas
    if inventaire_joueur == {}:
        print("Votre inventaire est vide. Aucune option possible.")
        return
    else:
        print("Voici votre inventaire actuel :")
        for cle in inventaire_joueur.keys():
            print(f"- {cle}")
    

def inventaire_ou_non(): #donnner un input de l'utilisateur
    print("Voulez-vous consulter votre inventaire ? (entrez i ou autre pour continuer sans consulter)")
    choix = input().lower() #marche si capslock est activé
    if choix == "i":
        return True
    else :
        return False
    


def afficher_stat_joueur(stat_joueur, stat_precedente=None):


    print("\nStatistiques actuelles de l'étudiant(e):\n")

    configs = [ # Liste des clés à afficher avec leurs couleurs et valeurs maximales
        ("points de vie", VERT_VIF, 100),
        ("vie sociale", JAUNE,100),
        ("points de connaissances", BLEU_VIF, 100),
        ("multiplicateur de connaissances", MAUVE, None) # Pas de max pour le multiplicateur
    ]

    for cle, couleur, valeur_max in configs:
        valeur_actuelle = stat_joueur[cle]
        texte_diff = ""
        if stat_precedente is not None and cle in stat_precedente:
            diff = valeur_actuelle - stat_precedente[cle] # Calcul de la différence entre ancienne stat et nouvelle

            if isinstance(diff, float): # Arrondi les floats pour éviter les affichages longs genre (+0.3000004)
                diff = round(diff, 2)

            if diff > 0:
                texte_diff = f" {VERT}(+{diff}){RESET}" #si la difference est +, affiche en vert celle-ci
            elif diff < 0:
                texte_diff = f" {ROUGE}({diff}){RESET}" # de même mais si c est negatif, en rouge
        
        texte_max = f"/{valeur_max}" if valeur_max is not None else "" # Gestion de l'affichage des valeurs maximales
        
        print(f"{couleur}{cle} : {round(valeur_actuelle,1)}{texte_max}{RESET}{texte_diff}\n") #arrondissement de la valeur actuelle à 1 décimale