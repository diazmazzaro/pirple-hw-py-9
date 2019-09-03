
from Vehicle import Vehicle

class Car(Vehicle):
  # Car's constructor (extended from Vehicle) (make and model args are required)
  def __init__(self, make, model, year='Default', weight=1000, maintenance=False, trips=0, isDriving = False):
    Vehicle.__init__(self, make, model, year, weight, maintenance, trips)
    self.isDriving = isDriving


  # Set isDriving attribute
  def setIsDriving(self, isDriving):
    if not isDriving and self.isDriving:
      self.setTripsSinceMaintenance(self.getTripsSinceMaintenance() + 1)
    return self.isDriving

  # getters
  # Get isDriving attribute
  def getIsDriving(self):
    return self.isDriving

  # Drive set isDriving to True
  def Drive(self):
    self.setIsDriving(True)

  # Drive set isDriving to Fals
  def Stop(self):
    self.setIsDriving(False)

  def ShowInfo(self):
    temp = ''' \033[1;31;40mCar: \033[0;37;40m {}
  \033[1;35;40m┣━\033[0;37;40m Make  :\033[1;33;40m  {}\033[0;37;40m
  \033[1;35;40m┣━\033[0;37;40m Model :\033[1;33;40m  {}\033[0;37;40m
  \033[1;35;40m┣━\033[0;37;40m Year  :\033[1;33;40m  {}\033[0;37;40m
  \033[1;35;40m┣━\033[0;37;40m weight:\033[1;33;40m  {}\033[0;37;40m
  \033[1;35;40m┣━\033[0;37;40m NeedsMaintenance:\033[1;33;40m  {}\033[0;37;40m
  \033[1;35;40m┗━\033[0;37;40m TripsSinceMaintenance: \033[1;33;40m {} \033[0;37;40m
    '''
    print(temp.format(self.model + '-' + str(self.year), self.make, self.model, self.year, self.weight, self.needsMaintenance, self.tripsSinceMaintenance))


