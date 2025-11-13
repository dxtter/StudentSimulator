from models.encounter import choixdispo
def afficher_choix_debase():
    print(f"Le premier choix est : {choixdispo()[0]}\nLe deuxième choix est : {choixdispo()[1]}\nLe troisième choix est : {choixdispo()[2]}")

    