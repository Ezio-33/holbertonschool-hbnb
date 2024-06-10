
#!/usr/bin/python3
"""
Module contenant la classe Utilisateur.
"""

import uuid
from datetime import datetime

class Utilisateur:
    """
    Classe représentant un utilisateur.
    """
    def __init__(self, email: str, mot_de_passe: str, prenom: str, nom_de_famille: str):
        self.id = uuid.uuid4()
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.prenom = prenom
        self.nom_de_famille = nom_de_famille
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
