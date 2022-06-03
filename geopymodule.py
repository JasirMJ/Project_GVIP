# importing geopy library
import requests
from geopy.geocoders import Nominatim
#
# # calling the Nominatim tool
# loc = Nominatim(user_agent="GetLoc")
#
# # entering the location name
# getLoc = loc.geocode("Gosainganj Lucknow")
#
# # printing address
# print(getLoc.address)
#
# # printing latitude and longitude
# print("Latitude = ", getLoc.latitude, "\n")
# print("Longitude = ", getLoc.longitude)


freegeoip = "http://freegeoip.net/json"
geo_r = requests.get(freegeoip)
geo_json = geo_r.json()
print(geo_json)

user_postition = [geo_json["latitude"], geo_json["longitude"]]