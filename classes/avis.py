#!/usr/bin/python3
"""
Module contenant la classe Avis.
"""

import uuid
from datetime import datetime
from utilisateur import Utilisateur
from lieu import Lieu

class Avis:
    """
    Classe représentant un avis.
    """
    def __init__(self, commentaire: str, note: int, utilisateur: Utilisateur, lieu: Lieu):
        self.id = uuid.uuid4()
        self.commentaire = commentaire
        self.note = note
        self.utilisateur_id = utilisateur.id
        self.lieu_id = lieu.id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    @property
    def commentaire(self):
        return self.__commentaire
    
    @commentaire.setter
    def commentaires(self, value):
        if not isinstance(value, str):
            raise TypeError("le commentaire doit etre une chaine de caractere")
        self.__commentaire = value

    @property
    def note(self):
        return self.__note
    
    @note.setter
    def note(self, value):
        if not isinstance(value, str):
            raise TypeError("la note doit etre un entier")
        self.__note = value

    @property
    def created_at(self):
        return self.__created_at
    
    @created_at.setter
    def created_at(self, value):
        if not isinstance(value, datetime):
            raise TypeError("created_at doit être une instance de date et d’heure")
        self.__created_at = value

    @property
    def updated_at(self):
        return self.__updated_at
    
    @updated_at.setter
    def updated_at(self, value):
        if not isinstance(value, datetime):
            raise TypeError("updated_at doit être une instance de date et d’heure")
        self.__updated_at = value

    @property
    def utilisateur_id(self):
        return self.__utilisateur_id
    
    @utilisateur_id.setter
    def utilisateur_id(self, value):
        if not isinstance(value, uuid) or value is None:
            raise TypeError("utilisateur_id doit être un UUID non vide")
        self.__utilisateur_id = value

    @property
    def lieu_id(self):
        return self.__lieu_id
    
    @lieu_id.setter
    def lieu_id(self, value):
        if not isinstance(value, uuid) or value is None:
            raise TypeError("lieu_id doit être un UUID non vide")
        self.__lieu_id = value
