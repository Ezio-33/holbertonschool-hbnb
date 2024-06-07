#!/usr/bin/python3
"""
Module contenant la classe Date.
"""

import uuid
from datetime import datetime

class Date:
    """
    Classe représentant une date.
    """
    def __init__(self):
        self.id = uuid.uuid4()
        self.date_creation = datetime.now()
        self.date_mise_a_jour = datetime.now()

    def ajouter(self):
        pass

    def modifier(self):
        pass

    def supprimer(self):
        pass
