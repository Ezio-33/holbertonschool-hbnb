#!/usr/bin/python3
"""
Module contenant l'interface de gestion de la persistance des données.
"""

from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    """
    Interface pour la gestion de la persistance des données.
    """
    @abstractmethod
    def save(self, entity):
        """
        Sauvegarde une entité dans le stockage.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Récupère une entité basée sur son ID et son type.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Met à jour une entité dans le stockage.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Supprime une entité du stockage.
        """
        pass