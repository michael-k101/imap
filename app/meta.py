
# meta.py
# File that contains all the functions necessary
# to extract meta data from the images.

import requests
import exifread as ef

# barrowed from 
# https://gist.github.com/snakeye/fdc372dbf11370fe29eb 
# Converts meta tag format to a readable latitude and longitude.
def _convert_to_degress(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)

# Extracts GPS information from and image.
def get_gps(filepath):
    with open(filepath, 'rb') as f:
        tags = ef.process_file(f)
        latitude = tags.get('GPS GPSLatitude')
        latitude_ref = tags.get('GPS GPSLatitudeRef')
        longitude = tags.get('GPS GPSLongitude')
        longitude_ref = tags.get('GPS GPSLongitudeRef')
        if latitude:
            lat_value = _convert_to_degress(latitude)
            if latitude_ref.values != 'N':
                lat_value = -lat_value
        else:
            return None, None
        if longitude:
            lon_value = _convert_to_degress(longitude)
            if longitude_ref.values != 'E':
                lon_value = -lon_value
        else:
            return None, None
        return lat_value, lon_value
    return None, None

# Reverse geocodes latitude and longitude
# and returns an address using the Google
# API.
def reverse_geocode(lat, lon):
    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
    
    parameters = {
        'key': 'your-api-key',
        'latlng': str(lat) + ',' + str(lon)
    }

    request = requests.get(GOOGLE_MAPS_API_URL, params=parameters)
    response = request.json()
    result = response['results']

    if (result):
        address = result[0]['formatted_address']
        if (address):
            return address
        else:
            return None
    else:
        return None

def get_date(filepath):
    with open(filepath, 'rb') as f:
        tags = ef.process_file(f)
        if (tags):
            return(tags['Image DateTime'])
        else:
            return None

# Counter for new file naming scheme.
counter = 1

# Generates new file name based on address
# and date created.
def create_new_name(address, date):
    global counter
    if (address and date):
        comma_index = address.index(',')
        space_index = date.index(' ')
        prefix = address[0:comma_index].replace(' ','')
        root = date[0:space_index].replace(':', '-')
        suffix = str(counter)
    elif (address != None):
        comma_index = address.index(',')
        prefix = address[0:comma_index]
        root = 'NA'
        suffix = str(counter)
    elif (date != 'None'):
        space_index = date.index(' ')
        prefix = 'NA'
        root = date[0:space_index].replace(':', '-')
        suffix = str(counter)
    else:
        prefix = 'NA'
        root = 'NA'
        suffix = str(counter)
    new_name = prefix + '_' + root + '_' + suffix + '.jpg'
    counter += 1
    return new_name
