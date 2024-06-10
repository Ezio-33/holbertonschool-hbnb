#!/usr/bin/python3
"""
Module contenant la classe Ville.
"""

import uuid
from pays import Pays

class Ville:
    """
    Classe représentant une ville.
    """
    def __init__(self, nom: str, pays: Pays):
        self.id = uuid.uuid4()
        self.nom = nom
        self.pays_id = pays.id
