#  _    ___          __     ___  
# | |  | \ \        / /    / _ \ 
# | |__| |\ \  /\  / /____| (_) |
# |  __  | \ \/  \/ /______\__, |
# | |  | |  \  /\  /         / / 
# |_|  |_|   \/  \/         /_/  
#

from Vehicle import Vehicle
from Car import Car

fordFiesta = Car("Ford", "Fiesta", 2000, 1010)
hondaCivic = Car("Honda", "Civic", 2019, 1981)
toyotaCelica = Car("Toyota", "Celica", 1997, 989)

def ShowCars():
  fordFiesta.ShowInfo()
  hondaCivic.ShowInfo()
  toyotaCelica.ShowInfo()


ShowCars()