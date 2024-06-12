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

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        if not isinstance(value, str):
            raise TypeError("le nom doit etre une chaine de caractere")
        self.__nom = value

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("la description doit etre une chaine de caractere")
        self.__description = value