import time
from models.mongua import Mongua



class Board(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('title', str, ''),
    ]