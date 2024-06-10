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
