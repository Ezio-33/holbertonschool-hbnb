#!/usr/bin/python3
"""
Module contenant la classe Date.
"""

import uuid
from datetime import datetime

class Date:
    """
    Classe représentant une date.
    """
    def __init__(self):
        self.id = uuid.uuid4()
        self.date_creation = datetime.now()
        self.date_mise_a_jour = datetime.now()

    @property
    def date_creation(self):
        return self.__date_creation
    
    @date_creation.setter
    def date_creation(self, value):
        if not isinstance(value, datetime):
            raise TypeError("date_creation doit être une instance de datetime")
        self.__date_creation = value

    @property
    def date_mise_a_jour(self):
        return self.__date_mise_a_jour
    
    @date_mise_a_jour.setter
    def date_mise_a_jour(self, value):
        if not isinstance(value, datetime):
            raise TypeError("date_mise_a_jour doit être une instance de datetime")
        self.__date_mise_a_jour = value

    def to_dict(self):
        """
        Convertit l'objet Date en dictionnaire.
        """
        return {
            'id': str(self.id),
            'date_creation': self.date_creation.isoformat(),
            'date_mise_a_jour': self.date_mise_a_jour.isoformat()
        }
