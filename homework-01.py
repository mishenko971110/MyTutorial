import math

RADIUS = 6371.01

lat1 = math.radians(50.45)
lon1 = math.radians(30.523)

lat2 = math.radians(51.5072)
lon2 = math.radians(-0.1275)

distance = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

#lat1_radians = math.radians(lat1)
#lon1_radians = math.radians(lon1)
#lat2_radians = math.radians(lat2)
#lon2_radians = math.radians(lon2)

#distance = 6371.01 * math.acos(math.sin(lat1_radians) * math.sin(lat2_radians) + math.cos(lat1_radians) * math.cos(lat2_radians) * math.cos(lon1_radians - lon2_radians))

