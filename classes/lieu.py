#!/usr/bin/python3
"""
Module contenant la classe Lieu.
"""

import uuid
from datetime import datetime
from typing import List
from ville import Ville
from utilisateur import Utilisateur
from commodite import Commodite
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
