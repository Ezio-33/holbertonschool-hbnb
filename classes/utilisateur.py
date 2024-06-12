#!/usr/bin/python3
"""
Module contenant la classe Utilisateur.
"""

import uuid
from datetime import datetime

class Utilisateur:
    """
    Classe représentant un utilisateur.
    """
    def __init__(self, email: str, mot_de_passe: str, prenom: str, nom_de_famille: str):
        self.id = uuid.uuid4()
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.prenom = prenom
        self.nom_de_famille = nom_de_famille
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("cette email existe déja")
        self._email = value

    @property
    def mot_de_passe(self):
        return self.__mot_de_passe
    
    @mot_de_passe.setter
    def mot_de_passe(self, value):
        if not isinstance(value, str):
            raise TypeError("le mot de passe doit contenir 8 caractère")
        self.__mot_de_passe = value

    @property
    def prenom(self):
        return self._prenom
    
    @prenom.setter
    def prenom(self, value):
        if not isinstance(value, str):
            raise TypeError("le prenom doit etre une chaine de caractere")
        self._prenom = value

    @property
    def nom_de_famille(self):
        return self.__nom_de_famille
    
    @nom_de_famille.setter
    def nom_de_famille(self, value):
        if not isinstance(value, str):
            raise TypeError("le nom_de_famille doit etre une chaine de caractere")
        self.__nom_de_famille = value

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

    def to_dict(self):
        """
        Convertit l'objet Utilisateur en dictionnaire.
        """
        return {
            'id': str(self.id),
            'email': self.email,
            'mot_de_passe': self.mot_de_passe,
            'prenom': self.prenom,
            'nom_de_famille': self.nom_de_famille,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }