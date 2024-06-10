import unittest
from uuid import uuid4
from data_manager import DataManager
from utilisateur import Utilisateur
from lieu import Lieu
from ville import Ville
from pays import Pays

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager(storage_file='test_data.json')
        self.data_manager.data = {}  # Reset data for each test

    def test_save_and_get_user(self):
        user = Utilisateur("test@example.com", "password", "John", "Doe")
        self.data_manager.save(user)
        retrieved_user = self.data_manager.get(user.id, Utilisateur)
        self.assertIsNotNone(retrieved_user)
        # Asserting individual attributes
        self.assertEqual(retrieved_user['email'], "test@example.com")
        self.assertEqual(retrieved_user['mot_de_passe'], "password")
        self.assertEqual(retrieved_user['prenom'], "John")
        self.assertEqual(retrieved_user['nom_de_famille'], "Doe")

    def test_update_user(self):
        user = Utilisateur("test@example.com", "password", "John", "Doe")
        self.data_manager.save(user)
        user.prenom = "Jane"
        self.data_manager.update(user)
        retrieved_user = self.data_manager.get(user.id, Utilisateur)
        self.assertEqual(retrieved_user['prenom'], "Jane")

    def test_delete_user(self):
        user = Utilisateur("test@example.com", "password", "John", "Doe")
        self.data_manager.save(user)
        self.data_manager.delete(user.id, Utilisateur)
        retrieved_user = self.data_manager.get(user.id, Utilisateur)
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()
