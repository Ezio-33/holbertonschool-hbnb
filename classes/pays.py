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

    def to_dict(self):
        """
        Convertit l'objet Pays en dictionnaire.
        """
        return {
            'id': str(self.id),
            'nom': self.nom
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Création d'une instance de la classe Lieu avec les valeurs du dictionnaire
        """
        instance = cls(
            nom=data['nom'],
        )
        """
        Assigner l'ID depuis le dictionnaire à l'instance
        """
        instance.id = uuid.UUID(data['id'])
        return instance
