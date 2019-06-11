def geocode(address):
    import googlemaps as gm
    # Your_GeocodingAPI_KEY
    gmaps_key = gm.Client(key='Your_GeocodingAPI_KEY')

    geocoder_res = gmaps_key.geocode(address)
    try:
        lat = geocoder_res[0]['geometry']['location']['lat']
        lon = geocoder_res[0]['geometry']['location']['lng']
    except:
        lat = None
        lon = None

    return lat,lon


def fetchData(lat,lng):
    from urllib.request import urlopen
    import json
    #YOUR_OpenWeatherMaps_API_key
    weatherAPI = '#YOUR_OpenWeatherMaps_API_key'
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat,lng,weatherAPI)
    with urlopen(url) as respons:
        pureResponse = respons.read()
    data = json.loads(pureResponse)
    return data

def displayData(data):
    temp_max = data['main']['temp_max']
    temp_min = data['main']['temp_min']
    windspeed = data['wind']['speed']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    sunrise = int(data['sys']['sunrise'])
    sunset = int(data['sys']['sunset'])
    import time
    sunset = time.strftime('%m/%d/%Y %H:%M:%S',  time.localtime(sunset))
    sunrise = time.strftime('%m/%d/%Y %H:%M:%S',  time.localtime(sunrise))
    print('========================')
    print('======WEATHER REPORT for {}======'.format(data['name'].upper()))
    print('Min. Temp : {} Fahrenheit'.format(temp_min))
    print('Max. Temp : {} Fahrenheit'.format(temp_max))
    print('Windspeed : {} mps'.format(windspeed))
    print('Humidity : {}%'.format(humidity))
    print('Pressure : {} hPa'.format(pressure))
    print('SUNRISE : {}'.format(sunrise))
    print('SUNSET : {}'.format(sunset))
    print('Latitude : {}'.format(data['coord']['lat']))
    print('Longitude : {}'.format(data['coord']['lon']))
    print('*Time displayed for Sunrise and Sunset is based on your PC\'s local timezone')



#Main
print('======Hello , Welcome to WeatherForecast======')
print('1.Using Latitute,Longitude')
print('2.Using City Name')
choice = input('CHOICE-->')
if choice == '1':
    lat = float(input('Enter Latitude : '))
    lng = float(input('Enter Longitude : '))
elif choice == '2':
    city = input('Enter City name : ')
    lat,lng = geocode(city)

showData = fetchData(lat,lng)
displayData(showData)