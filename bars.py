import json
from math import radians, cos, sin, asin, sqrt


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file_handler:
        _data_ = json.load(file_handler)
    return _data_


def get_biggest_bar(data):
    return max(data["features"], key=lambda x: x["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(data):
    return min(data["features"], key=lambda x: x["properties"]["Attributes"]["SeatsCount"])


def get_closest_bar(data, longitude, latitude):
    return min(data["features"], key=lambda x: distance(x["geometry"]["coordinates"], longitude, latitude))


def distance(bar_coordinates, longitude, latitude):
    """
    Calculate the great circle distance between bar and point coordinate
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [bar_coordinates[0], bar_coordinates[1], longitude, latitude])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    earth_radius = 6371
    km = earth_radius * c
    return km


if __name__ == '__main__':
    bars_data_file = "bars.json"
    bars_data = load_data(bars_data_file)
    biggest = get_biggest_bar(bars_data)
    smallest = get_smallest_bar(bars_data)
    closest = get_closest_bar(bars_data, 37.603167143241507, 55.623358258831558)
    print(biggest["properties"]["Attributes"]["Name"], biggest["properties"]["Attributes"]["SeatsCount"])
    print(smallest["properties"]["Attributes"]["Name"], smallest["properties"]["Attributes"]["SeatsCount"])
    print(closest["properties"]["Attributes"]["Name"])
