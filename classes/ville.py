
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

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        if not isinstance(value, str):
            raise TypeError("le nom doit etre une chaine de caractere")
        self.__nom = value

    @property
    def pays_id(self):
        return self.__pays_id
    
    @pays_id.setter
    def pays_id(self, value):
        if not isinstance(value, uuid) or value is None:
            raise TypeError("pays_id doit être un UUID non vide")
        self.__pays_id = value

    def to_dict(self):
        """
        Convertit l'objet Ville en dictionnaire.
        """
        return {
            'id': str(self.id),
            'nom': self.nom,
            'pays_id': str(self.pays_id)
        }