
from Vehicle import Vehicle

class Car(Vehicle):

  def __init__(self, make, model, year='Default', weight=1000, maintenance=False, trips=0):
    Vehicle.__init__(make, model, year, weight, maintenance, trips)