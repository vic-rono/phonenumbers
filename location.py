import phonenumbers

import folium
from number import num

from phonenumbers import geocoder

from opencage.geocoder import OpenCageGeocode

apiKey = "weka yako from opencage"
perNumber = phonenumbers.parse(num)

perLocation = geocoder.description_for_number(perNumber, "en")
print(perLocation)

# serviceprovider

from phonenumbers import carrier

service_provider = phonenumbers.parse(num)

print(carrier.name_for_number(service_provider, "en"))

print

gc = OpenCageGeocode(apiKey)

res = gc.geocode(str(perLocation))

print(res)

#lat = res[0]['geometry']['lat']
#lng = res[0]['annotations']['lng']
#print(lat, lng)

#map = folium.Map(location=[lat,lng], zoom_start = 9)

#folium.Marker([lat,lng], popup=perLocation).add_to((map))

#map.save("perLocation.html")
