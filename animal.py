class Habitat:
    pass

class Tete:
    pass

class Corp:
    pass

class Membres:
    pass

class Animal:
    def __init__(self, habitat: Habitat, tete: Tete, corp: Corp):
        self.habitat = habitat
        self.tete = tete
        self.corp = corp
        self.membres = []  # Liste pour les membres de l'animal

    def ajouterMembre(self, membre: Membres):
        self.membres.append(membre)
