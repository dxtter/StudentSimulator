def afficher_choix_debase():
    file_path = 'models/encounter.py'
    f = open(file_path, encoding = "utf-8")
    print(choix_dispo())
    f.close()