#!/usr/bin/python3
"""
Module contenant la classe Lieu.
"""

import uuid
from datetime import datetime
from typing import List, TYPE_CHECKING
from ville import Ville
from utilisateur import Utilisateur
from commodite import Commodite

if TYPE_CHECKING:
    from avis import Avis

class Lieu:
    """
    Classe représentant un lieu.
    """
    def __init__(self, nom: str, description: str, adresse: str, ville: Ville,
                 latitude: float, longitude: float, hote: Utilisateur,
                 chambres: int, salles_de_bains: int, prix_par_nuit: float,
                 max_invites: int):
        self.id = uuid.uuid4()
        self.nom = nom
        self.description = description
        self.adresse = adresse
        self.ville_id = ville.id
        self.latitude = latitude
        self.longitude = longitude
        self.hote_id = hote.id
        self.chambres = chambres
        self.salles_de_bains = salles_de_bains
        self.prix_par_nuit = prix_par_nuit
        self.max_invites = max_invites
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.commodites = []
        self.avis = []

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

    @property
    def adresse(self):
        return self.__adresse
    
    @adresse.setter
    def adresse(self, value):
        if not isinstance(value, str):
            raise TypeError("l'adresse doit etre une chaine de caractere")
        self.__adresse = value

    @property
    def chambres(self):
        return self.__chambres
    
    @chambres.setter
    def chambres(self, value):
        if not isinstance(value, int):
            raise TypeError("la chambres doit etre un entier")
        self.__chambres = value

    @property
    def salles_de_bains(self):
        return self.__salles_de_bains
    
    @salles_de_bains.setter
    def salles_de_bains(self, value):
        if not isinstance(value, int):
            raise TypeError("la salle de bain doit etre un entier")
        self.__salles_de_bains = value

    @property
    def prix_par_nuit(self):
        return self.__prix_par_nuit
    
    @prix_par_nuit.setter
    def prix_par_nuit(self, value):
        if not isinstance(value, float):
            raise TypeError("le prix par nuit doit etre un float")
        self.__prix_par_nuit = value

    @property
    def max_invites(self):
        return self.__max_invites
    
    @max_invites.setter
    def max_invites(self, value):
        if not isinstance(value, int):
            raise TypeError("le max d'invités doit etre un entier")
        self.__max_invites = value

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
    def ville_id(self):
        return self.__ville_id
    
    @ville_id.setter
    def ville_id(self, value):
        if not isinstance(value, uuid) or value is None:
            raise TypeError("ville_id doit être un UUID non vide")
        self.__ville_id = value

    @property
    def hote_id(self):
        return self.__hote_id
    
    @hote_id.setter
    def hote_id(self, value):
        if not isinstance(value, uuid) or value is None:
            raise TypeError("hote_id doit être un UUID non vide")
        self.__hote_id = value
