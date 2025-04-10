import phonenumbers
import opencage 
import folium

from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

number = "+33768720030"


pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber , "fr")
print (location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "fr" ))

key = "9fb018e62d3d45eea923bea060b3df32"

geocoder = OpenCageGeocode(key)
query= str(location)
results= geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']["lat"]
lng = results[0]['geometry']["lng"]

print(lat,lng)

myMap = folium.Map(location= [lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")

