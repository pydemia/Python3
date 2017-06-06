
# Google Maps Geocode API Example


```python
import googlemaps as gm
```


```python
gmapsClient = gm.Client(key='AIzaSyD3hyIgUZotbLboevi38kgWhFPisaxw6rw')
```

## 1. Get Geocode from Address


```python
myaddress = '서울특별시 강남구 영동대로 513'  # COEX Address
```


```python
geoDict = gmapsClient.geocode(myaddress, language='ko')[0]  # It returns a list contains a dict only
type(geoDict)
```




    dict




```python
geoDict
```




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




```python
print(geoDict['formatted_address'])
print(geoDict['geometry']['location'])
```

    대한민국 서울특별시 강남구 영동대로 513
    {'lat': 37.5101935, 'lng': 127.0585824}


## 2. Get Address from Geocode


```python
gmapsClient.reverse_geocode((37.5101935, 127.0585824), language='ko')[0]
```




    {'address_components': [{'long_name': '159',
       'short_name': '159',
       'types': ['political', 'premise']},
      {'long_name': '삼성1동',
       'short_name': '삼성1동',
       'types': ['political', 'sublocality', 'sublocality_level_2']},
      {'long_name': '강남구',
       'short_name': '강남구',
       'types': ['political', 'sublocality', 'sublocality_level_1']},
      {'long_name': '서울특별시',
       'short_name': '서울특별시',
       'types': ['locality', 'political']},
      {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']},
      {'long_name': '135-091', 'short_name': '135-091', 'types': ['postal_code']}],
     'formatted_address': '대한민국 서울특별시 강남구 삼성1동 159',
     'geometry': {'location': {'lat': 37.5101935, 'lng': 127.0585824},
      'location_type': 'ROOFTOP',
      'viewport': {'northeast': {'lat': 37.5115424802915,
        'lng': 127.0599313802915},
       'southwest': {'lat': 37.5088445197085, 'lng': 127.0572334197085}}},
     'place_id': 'ChIJC3bBJmukfDURjTSmaADkHWs',
     'types': ['political', 'premise']}


