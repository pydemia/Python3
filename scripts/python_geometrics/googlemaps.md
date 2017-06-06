# `googlemaps`


## Installation

```sh
pip install googlemaps
```

## Get Google Maps API

Set [here](https://developers.google.com/maps/)

* Address & Coordinates : [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/start)  
Mine : AIzaSyD3hyIgUZotbLboevi38kgWhFPisaxw6rw  
* Distances : [Google Maps Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/)  
Mine : AIzaSyDcR76D4dh7A2V_ERzn89-PJ5z8OLPh6xI
* Directions & Paths : [Google Maps Directions API](https://developers.google.com/maps/documentation/directions/)  
Mine : AIzaSyAY1rBsdeUQ83WV4JqG-vmQG-74N2DZmB0  


```py
import googlemaps as gm


gmapsClient = gm.Client(key='AIzaSyD3hyIgUZotbLboevi38kgWhFPisaxw6rw')
```

### Get Geocode from an Address
```py
myaddress = '서울특별시 강남구 영동대로 513'  # COEX Address
geoDict = gmapsClient.geocode(myaddress, language='ko')[0]  # It returns a list contains a dict only
type(geoDict)
geoDict
```

```py
{'address_components': [{'long_name': '513',
   'short_name': '513',
   'types': ['political', 'premise']},
  {'long_name': '영동대로',
   'short_name': '영동대로',
   'types': ['political', 'sublocality', 'sublocality_level_4']},
  {'long_name': '강남구',
   'short_name': '강남구',
   'types': ['political', 'sublocality', 'sublocality_level_1']},
  {'long_name': '서울특별시',
   'short_name': '서울특별시',
   'types': ['locality', 'political']},
  {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']},
  {'long_name': '135-090', 'short_name': '135-090', 'types': ['postal_code']}],
 'formatted_address': '대한민국 서울특별시 강남구 영동대로 513',
 'geometry': {'location': {'lat': 37.5101935, 'lng': 127.0585824},
  'location_type': 'ROOFTOP',
  'viewport': {'northeast': {'lat': 37.5115424802915,
    'lng': 127.0599313802915},
   'southwest': {'lat': 37.5088445197085, 'lng': 127.0572334197085}}},
 'place_id': 'ChIJC3bBJmukfDURsJODU-wM6bg',
 'types': ['political', 'premise']}
```

```py
print(geoDict['formatted_address'])
print(geoDict['geometry']['location'])
```

### Get an Address from its Geocode
```py
gmapsClient.reverse_geocode((37.5101935, 127.0585824), language='ko')[0]
```




