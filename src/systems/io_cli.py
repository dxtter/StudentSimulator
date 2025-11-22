from models.encounter import choixdispo
RESET = "\033[0m"
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


"""def afficher_stat_joueur(stat_joueur): #fonction servant à afficher les barres (stats principales du joueur)

    print("\nStatistiques actuelles de l'étudiant(e):\n")
    print (f"{VERT_VIF}Points de vie :{stat_joueur['points de vie']}/10{RESET}\n\n{JAUNE}Vie sociale :{stat_joueur['vie sociale']}/100{RESET}\n\n{BLEU_VIF}Points de connaissances :{stat_joueur['points de connaissances']}/100{RESET}\n\n{MAUVE}Multiplicateur de connaissances :{stat_joueur['multiplicateur de connaissances']}{RESET}\n")
    #Daniel : j'ai ajouté le multiplicateur de connaissances """

def affichage_apres_epreuve(reussite):
    if reussite :
        print(f"{VERT}Bien joué ! Vous vous en êtes tirés pour cette fois mais l'année n'est pas encore finie Mouhahahaha{RESET}")
    elif not reussite:
        print(f"{ROUGE}Vous n'êtes qu'un bon à rien, revenez plus fort pour une prochaine épreuve, mais surveillez votre barre de vie SKIBIDI{RESET}")


def afficher_recompenses_au_joueur(dico_reco):
    print("Voici les récompenses parmi lesquelles vous pouvez choisir :")
    for i, cle in enumerate(dico_reco.keys(), start=1):
        print(f"{i}) {cle}")

def afficher_inventaire_du_joueur(inventaire_joueur): #donner un dico d'inventaire, oui_ou_non bool pour savoir si on affiche l'inventaire ou pas
    
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

    # Liste des clés à afficher avec leurs couleurs et max values
    # Format: (Clé, Couleur, MaxValue)
    configs = [
        ("points de vie", VERT_VIF, 100),
        ("vie sociale", JAUNE,100),
        ("points de connaissances", BLEU_VIF, 100),
        ("multiplicateur de connaissances", MAUVE, None) # Pas de max pour le multi
    ]

    for cle, couleur, valeur_max in configs:
        valeur_actuelle = stat_joueur[cle]
        
        # Calcul du texte de différence entre ancienne stat et nouvelle
        texte_diff = ""
        if stat_precedente is not None and cle in stat_precedente:
            diff = valeur_actuelle - stat_precedente[cle]
            
            # On arrondit les floats pour éviter les affichages genre (+0.3000004)
            if isinstance(diff, float):
                diff = round(diff, 2)

            if diff > 0:
                texte_diff = f" {VERT}(+{diff}){RESET}"
            elif diff < 0:
                texte_diff = f" {ROUGE}({diff}){RESET}"
        
        # Gestion de l'affichage "/Max"
        texte_max = f"/{valeur_max}" if valeur_max is not None else ""
        
        # Affichage final de la ligne
        print(f"{couleur}{cle} : {valeur_actuelle}{texte_max}{RESET}{texte_diff}\n")