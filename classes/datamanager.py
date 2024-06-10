#!/usr/bin/python3
"""
Module contenant la classe DataManager pour la gestion de la persistance des données.
"""

import json
import os
from uuid import UUID
from typing import Type
from datetime import datetime
from i_persistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    """
    Classe de gestion des données implémentant l'interface IPersistenceManager.
    """
    def __init__(self, storage_file='data.json'):
        self.storage_file = storage_file
        self.data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return {}

    def _save_data(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.data, file)

    def save(self, entity):
        entity_id = str(entity.id)
        entity_type = entity.__class__.__name__
        if entity_type not in self.data:
            self.data[entity_type] = {}
        self.data[entity_type][entity_id] = entity.__dict__
        self._save_data()

    def get(self, entity_id: UUID, entity_type: Type):
        entity_type_name = entity_type.__name__
        entity_id_str = str(entity_id)
        if entity_type_name in self.data and entity_id_str in self.data[entity_type_name]:
            return self.data[entity_type_name][entity_id_str]
        return None

    def update(self, entity):
        entity_id = str(entity.id)
        entity_type = entity.__class__.__name__
        if entity_type in self.data and entity_id in self.data[entity_type]:
            self.data[entity_type][entity_id] = entity.__dict__
            self._save_data()

    def delete(self, entity_id: UUID, entity_type: Type):
        entity_type_name = entity_type.__name__
        entity_id_str = str(entity_id)
        if entity_type_name in self.data and entity_id_str in self.data[entity_type_name]:
            del self.data[entity_type_name][entity_id_str]
            self._save_data()