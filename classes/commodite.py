#!/usr/bin/python3
"""
Module contenant la classe Commodité.
"""

import uuid

class Commodite:
    """
    Classe représentant une commodité.
    """
    def __init__(self, nom: str, description: str):
        self.id = uuid.uuid4()
        self.nom = nom
        self.description = description

    def ajouter(self):
        pass

    def modifier(self):
        pass

    def supprimer(self):
        pass
