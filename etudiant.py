class Coordonnees:
    def __init__(self, adresse: str, telephone: str):
        self.adresse = adresse
        self.telephone = telephone

class Personne:
    def __init__(self, etatCivil: str, coordonnees: Coordonnees):
        self.etatCivil = etatCivil
        self.coordonnees = coordonnees

class Eleve(Personne):
    def __init__(self, etatCivil: str, coordonnees: Coordonnees):
        super().__init__(etatCivil, coordonnees)

class Professeur(Personne):
    def __init__(self, etatCivil: str, coordonnees: Coordonnees):
        super().__init__(etatCivil, coordonnees)

class Classe:
    def __init__(self, professeur: Professeur):
        self.professeur = professeur
        self.eleves = []

    def ajouter_eleve(self, eleve: Eleve):
        if len(self.eleves) < 30:
            self.eleves.append(eleve)
        else:
            raise Exception("La classe ne peut pas avoir plus de 30 élèves.")


