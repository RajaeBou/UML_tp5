class FichierJoint:
    def __init__(self, nom: str, taille: int, path: str):
        self.nom = nom
        self.taille = taille
        self.path = path


class Email:
    def __init__(self, expediteur: str, destination: str, titre: str = None, texte: str = None):
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destination = destination
        self.fichiers_joints = []

    def ajouter_fichier(self, fichier: FichierJoint):
        """Ajoute un fichier joint à l'email."""
        self.fichiers_joints.append(fichier)
