#  _    ___          __     ___  
# | |  | \ \        / /    / _ \ 
# | |__| |\ \  /\  / /____| (_) |
# |  __  | \ \/  \/ /______\__, |
# | |  | |  \  /\  /         / / 
# |_|  |_|   \/  \/         /_/  
#

from Vehicle import Vehicle
from Car import Car

generictVehicle = Vehicle('Ford', 'A')
generictCar = Vehicle('Ford', 'b')

print(generictVehicle.getMake())
print(generictCar.getMake())