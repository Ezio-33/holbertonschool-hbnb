import uuid
from datetime import datetime
import unittest
from utilisateur import Utilisateur
from pays import Pays
from ville import Ville
from lieu import Lieu
from avis import Avis
from commodite import Commodite

class TestClasses(unittest.TestCase):

    def test_utilisateur(self):
        user = Utilisateur(email="test@example.com", mot_de_passe="password123", prenom="John", nom_de_famille="Doe")
        self.assertIsInstance(user, Utilisateur)
        self.assertEqual(user.email, "test@example.com")

    def test_pays(self):
        country = Pays(nom="France")
        self.assertIsInstance(country, Pays)
        self.assertEqual(country.nom, "France")

    def test_ville(self):
        country = Pays(nom="France")
        city = Ville(nom="Paris", pays=country)
        self.assertIsInstance(city, Ville)
        self.assertEqual(city.nom, "Paris")
        self.assertEqual(city.pays_id, country.id)

    def test_lieu(self):
        country = Pays(nom="France")
        city = Ville(nom="Paris", pays=country)
        user = Utilisateur(email="test@example.com", mot_de_passe="password123", prenom="John", nom_de_famille="Doe")
        place = Lieu(nom="Nice Apartment", description="A very nice place", adresse="123 Main St", ville=city,
                     latitude=48.8566, longitude=2.3522, hote=user, chambres=2, salles_de_bains=1, prix_par_nuit=100.0,
                     max_invites=4)
        self.assertIsInstance(place, Lieu)
        self.assertEqual(place.nom, "Nice Apartment")

    def test_avis(self):
        country = Pays(nom="France")
        city = Ville(nom="Paris", pays=country)
        user = Utilisateur(email="test@example.com", mot_de_passe="password123", prenom="John", nom_de_famille="Doe")
        place = Lieu(nom="Nice Apartment", description="A very nice place", adresse="123 Main St", ville=city,
                     latitude=48.8566, longitude=2.3522, hote=user, chambres=2, salles_de_bains=1, prix_par_nuit=100.0,
                     max_invites=4)
        review = Avis(commentaire="Great place!", note=5, utilisateur=user, lieu=place)
        self.assertIsInstance(review, Avis)
        self.assertEqual(review.commentaire, "Great place!")
        self.assertEqual(review.note, 5)

    def test_commodite(self):
        amenity = Commodite(nom="WiFi", description="High-speed wireless internet")
        self.assertIsInstance(amenity, Commodite)
        self.assertEqual(amenity.nom, "WiFi")

if __name__ == '__main__':
    unittest.main()