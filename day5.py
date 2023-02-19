# import geopy
from geopy.geocoders import Nominatim
loc = Nominatim(user_agent='GetLoc')
getloc = loc.geocode("Nigeria")
print(getloc.address)