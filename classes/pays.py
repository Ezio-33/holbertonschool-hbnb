
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

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        if not isinstance(value, str):
            raise TypeError("le nom doit etre une chaine de caractere")
        self.__nom = value
