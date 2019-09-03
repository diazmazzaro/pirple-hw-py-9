import datetime

# Define a Vehicle class
class Vehicle:

  # Vehicle's constructor (make and model args are required)
  def __init__(self, make, model, year='Default', weight=1000, maintenance=False, trips=0):
    self.make = make
    self.model = model
    if year == 'Default':
      self.year = datetime.datetime.now().year
    else:
      self.year = year 
    self.weight = weight
    self.needsMaintenance = maintenance
    self.tripsSinceMaintenance = trips

  #setters
  # Set model attribute
  def setModel(self, model):
    self.model = model
  # Set make attribute
  def setMake(self, make):
    self.make = make
  # Set year attribute
  def setYear(self, year):
    self.year = year
  # Set weight attribute
  def setWeight(self, weight):
    self.weight = weight
  # Set needsMaintenance attribute
  def setNeedsMaintenance(self, needsMaintenance):
    self.needsMaintenance = needsMaintenance
  # Set tripsSinceMaintenance attribute
  def setTripsSinceMaintenance(self, tripsSinceMaintenance):
    self.tripsSinceMaintenance = tripsSinceMaintenance
    if self.tripsSinceMaintenance > 100:
      self.needsMaintenance = True

  # getters
  # Get model attribute
  def getModel(self):
    return self.model
  # Get make attribute
  def getMake(self):
    return self.make
  # Get year attribute
  def getYear(self):
    return self.year
  # Get weight attribute
  def getWeight(self):
    return self.weight
  # Set weight attribute
  def getNeedsMaintenance(self):
    return self.needsMaintenance
  # Set weight attribute
  def getTripsSinceMaintenance(self):
    return self.tripsSinceMaintenance

  # Removes needsMaintenance flag and resets trip counter
  def Repair(self):
    self.needsMaintenance = False
    self.tripsSinceMaintenance = 0
