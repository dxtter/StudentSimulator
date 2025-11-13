from models.encounter import choixdispo
def afficher_choix_debase():
    print(f"Le premier choix est : {choixdispo()[0]}\nLe deuxième choix est : {choixdispo()[1]}\nLe troisième choix est : {choixdispo()[2]}")

from models.encounter import nouvelles_actions
def afficher_autreschoix():
    print (f"1){nouvelles_actions()[0]}\n2){nouvelles_actions()[1]}\n3)){nouvelles_actions()[2]}")