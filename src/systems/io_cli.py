from models.encounter import choixdispo
def afficher_choix_debase():
    print(f"Le premier choix est : {choixdispo()[0]}\nLe deuxième choix est : {choixdispo()[1]}\nLe troisième choix est : {choixdispo()[2]}")

from models.encounter import autreschoix
def afficher_autreschoix():
    choixpossibles=autreschoix()
    print (f"1) {choixpossibles[0]}\n2) {choixpossibles[1]}\n3) {choixpossibles[2]}")

#from models.player import stat_joueur_copy
#def afficher_stat_joueur():
   # print (f"Points de vie : ")