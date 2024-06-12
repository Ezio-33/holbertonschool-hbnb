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


    def to_dict(self):
        """
        Convertit l'objet Commodite en dictionnaire.
        """
        return {
            'id': str(self.id),
            'nom': self.nom,
            'description': self.description,
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Création d'une instance de la classe Commodite avec les valeurs du dictionnaire
        """
        instance = cls(
            nom=data['nom'],
            description=data['description']
        )
        """
        Assigner l'ID depuis le dictionnaire à l'instance
        """
        instance.id = uuid.UUID(data['id']) 
        return instance