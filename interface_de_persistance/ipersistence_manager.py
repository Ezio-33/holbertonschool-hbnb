from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def ajouter(self):
        pass

    @abstractmethod
    def modifier(self):
        pass

    @abstractmethod
    def supprimer(self):
        pass

    @abstractmethod
    def connexion(self):
        pass

