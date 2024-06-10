#!/usr/bin/python3
"""
Module contenant la classe Avis.
"""

import uuid
from datetime import datetime
from utilisateur import Utilisateur

class Avis:
    """
    Classe représentant un avis.
    """
    def __init__(self, commentaire: str, note: int, utilisateur: Utilisateur, lieu_id: uuid.UUID):
        self.id = uuid.uuid4()
        self.commentaire = commentaire
        self.note = note
        self.utilisateur_id = utilisateur.id
        self.lieu_id = lieu_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def ajouter(self):
        pass

    def modifier(self):
        pass

    def supprimer(self):
        pass
