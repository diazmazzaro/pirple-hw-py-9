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
  def setModel(model):
    self.model = model
  # Set make attribute
  def setMake(make):
    self.make = make
  # Set year attribute
  def setYear(year):
    self.year = year
  # Set weight attribute
  def setWeight(weight):
    self.weight = weight
  # Set weight attribute
  def setNeedsMaintenance(needsMaintenance):
    self.needsMaintenance = needsMaintenance
  # Set weight attribute
  def setTripsSinceMaintenance(tripsSinceMaintenance):
    self.tripsSinceMaintenance = tripsSinceMaintenance

  # getters
  # Get model attribute
  def getModel():
    return self.model
  # Get make attribute
  def getMake():
    return self.make
  # Get year attribute
  def getYear():
    return self.year
  # Get weight attribute
  def getWeight():
    return self.weight
  # Set weight attribute
  def getNeedsMaintenance():
    return self.needsMaintenance
  # Set weight attribute
  def getTripsSinceMaintenance():
    return self.tripsSinceMaintenance
