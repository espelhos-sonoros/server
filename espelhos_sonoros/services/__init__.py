from .box import box
from espelhos_sonoros.service import app

class Box(object):

    def __init__(self):
        self.address = 'localhost'

    def update(self, other):
        self.address = other['address']


box(Box(), app)
