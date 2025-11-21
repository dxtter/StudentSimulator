

from models.encounter import trois_choix_recompense, action_choisie

dico_reco = trois_choix_recompense()
print(action_choisie(list(dico_reco.keys())))