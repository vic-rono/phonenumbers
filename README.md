# phonenumbers
Using geo-location data from Open Cage data API to get location based on the phone number.....sort of.

# Dependencies
the geocoder module helps in getting location of the phonenumber in conjuction with OpenCage API.
parse module will ascertain that the phone numbers are in the correct format.
Carrier module will get the carrier information

```
pip install phonenumbers
```
For accessing the geocoding API
```
pip install opencage
```
Geographic visualizations for getting the location based on the lattitudes and longitudes.
Utilizes Leaflet javascript library through Python API.
```
pip install folium
```

# Resources
- Phonenumbers https://pypi.org/project/phonenumbers/
- Mapping  https://pypi.org/project/folium/
- Co-ordinates (API) https://opencagedata.com/

# Sort....of?
The API is only limited to accessing the country as a whole but not a specific location, i guess the carrier limits such information.
~~Hopefully~~, will come across a better OSINT tool.

![Screenshot (128)](https://github.com/vic-rono/phonenumbers/assets/61822296/3236ace9-fdf0-430f-a7ea-7e2e5e0268f2)


