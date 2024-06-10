
#!/usr/bin/python3
"""
Module contenant la classe Pays.
"""

import uuid

class Pays:
    """
    Classe représentant un pays.
    """
    def __init__(self, nom: str):
        self.id = uuid.uuid4()
        self.nom = nom
