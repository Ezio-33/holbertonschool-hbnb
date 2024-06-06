from uuid import uuid4, UUID

class Avis:
    def __init__(self, avis_id: UUID, commentaire: str, note: int):
        self.avis_id = avis_id
        self._commentaire = commentaire
        self._note = note

    @property
    def commentaire(self):
        return self._commentaire
    
    @property
    def note(self):
        return self._note



class Pays:
    def __init__(self, nom: str):
        self.pays_id = uuid4()
        self._nom = nom

    @property
    def nom(self):
        return self._nom



class Ville:
    def __init__(self, nom: str, pays_id: UUID):
        self.ville_id = uuid4()
        self._nom = nom
        self.pays_id = pays_id

    @property
    def nom(self):
        return self._nom



class Commodite:
    def __init__(self, nom: str, description: str):
        self.commodite_id = uuid4()
        self._nom = nom
        self._description = description

    @property
    def nom(self):
        return self._nom
    
    @property
    def description(self):
        return self._description



class Utilisateur:
    def __init__(self, email: str, prenom: str, nom_de_famille: str, mod_de_passe: str, lieu_id: UUID):
        self.utilisateur_id = uuid4()
        self._email = email
        self._prenom = prenom
        self._nom_de_famille = nom_de_famille
        self._mod_de_passe = mod_de_passe
        self.lieu_id = lieu_id

    @property
    def email(self):
        return self._email
    
    @property
    def prenom(self):
        return self._prenom
    
    @property
    def nom_de_famille(self):
        return self._nom_de_famille
    
    @property
    def mod_de_passe(self):
        return self._mod_de_passe



class Lieu:
    def __init__(self, description: str, adresse: str, latitude: float,
                 longitude: float, prix_par_nuit: float, nombre_max_invites: int,
                 ville_id: UUID, utilisateur_id: UUID):
        self.lieu_id = uuid4()
        self._description = description
        self._adresse = adresse
        self._latitude = latitude
        self._longitude = longitude
        self._prix_par_nuit = prix_par_nuit
        self._nombre_max_invites = nombre_max_invites
        self.ville_id = ville_id
        self.utilisateur_id = utilisateur_id

    @property
    def description(self):
        return self._description
    
    @property
    def adresse(self):
        return self._adresse
    
    @property
    def latitude(self):
        return self._latitude
    
    @property
    def longitude(self):
        return self._longitude
    
    @property
    def prix_par_nuit(self):
        return self._prix_par_nuit
    
    @property
    def nombre_max_invites(self):
        return self._nombre_max_invites
