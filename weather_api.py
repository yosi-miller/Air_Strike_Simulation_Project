from datetime import datetime
from requests import get

KEY = '5430b1b4fc467b19df24d9d698c57c56'

def read_location(city):
    """

    :param city:
    :return: {'lat': value, 'lon': value}
    """
    LOCATION_URL = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={KEY}'
    try:
        response = get(LOCATION_URL)
    except Exception as e:
        print(e)
    else:
        result = [response.json()[0]['lat'], response.json()[0]['lon']]
        return result

def read_weather(city):
    """

    :param city:
    :return: מחזיר את מצב המזג אוויר הראשי
    """
    WEATEHER_URL = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={KEY}'
    try:
        response = get(WEATEHER_URL)
    except Exception as e:
        print(e)
    else:
        time_check = datetime(datetime.now().year, datetime.now().month, datetime.now().day + 1, 00, 00, 00)
        result = filter(lambda d: d["dt_txt"] == str(time_check), response.json()['list'])
        return {'main': list(result)[0]['weather'][0]['main']}


if __name__ == '__main__':
    # location = read_location('San Francisco')
    # print(*location)
    weather = read_weather('San Francisco')
    print(weather)
    # re = weather["list"]
    # check_data = time_check = datetime(datetime.now().year, datetime.now().month,datetime.now().day + 1,00, 00, 00)
    # for i in re:
    #     if i["dt_txt"] == str(time_check):
    #         print(i)
    # print(re)
    # # print(type(re))
    # time_check = datetime(datetime.now().year, datetime.now().month,datetime.now().day + 1,00, 00, 00)
    # print(str(time_check))
