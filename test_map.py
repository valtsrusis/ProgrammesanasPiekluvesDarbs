#importē requests bibliotēku, kas ļauj vienkārši nosūtīt HTTP pieprasījumus.
import requests

#izsaukta funkcija no iepriekšēja python faila.
def maps_function():

    #izmantota Google API atslēga, lai piešķirtu atļauju izmantot no tā uzņēmuma API.
    GOOGLE_API_KEY = 'AIzaSyB9WNy4lIYhQTZAZcKS5etg-HmXHZo6J18' 

    #izvēlētā adrese veikalā.
    address = 'Ausekļa iela 19-13'

    params = {
        'key' : GOOGLE_API_KEY,
        'address' : address
    }

    base_url = 'https://maps.googleapis.com/maps/api/staticmap?center=Williamsburg,Brooklyn,NY&zoom=13&size=400x400&markers=color:blue%7Clabel:S%7C11211%7C11206%7C11222&key=AIzaSyB9WNy4lIYhQTZAZcKS5etg-HmXHZo6J18'
    response = requests.get(base_url, params=params).json()
    response.keys()

    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']

    print(lat, lon)