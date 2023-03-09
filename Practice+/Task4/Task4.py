from math import radians, cos, sin, asin, sqrt
from zip_util import read_zip_all


def coord_distance(lat1, lon1, lat2, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    p = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    q = 2 * asin(sqrt(p))
    RADIUS_EARTH = 3963
    return (q * RADIUS_EARTH)


def loc_fun():
    zip_code = input('Enter a ZIP Code to lookup => ')
    zip_codes = read_zip_all()
    f = 0
    for sublist in zip_codes:
        if sublist[0] == zip_code:
            f = 1
            print('ZIP Code', zip_code, 'is in', sublist[3] + ',', sublist[4] + ',', sublist[5], 'country')
            break
    if f != 1:
        print('Code not found')


def zip_fun():
    city = input('Enter a city name to lookup => ').lower()
    state = input('Enter a state name to lookup => ').lower()
    zip_codes = read_zip_all()
    zip_codes_list = []
    for sublist in zip_codes:
        if sublist[3].lower() == city and sublist[4].lower() == state:
            city = sublist[3]
            state = sublist[4]
            zip_codes_list.append(sublist[0])
    if len(zip_codes_list) != 0:
        print('The following ZIP Code(s) found for', city, ',', state + ':', ", ".join(map(str, zip_codes_list)))
    else:
        print('Area not found')


def dist_fun():
    zip_code1 = input('Enter the first ZIP Code => ')
    zip_code2 = input('Enter the second ZIP Code => ')
    zip_codes = read_zip_all()
    not_found_codes = [zip_code1, zip_code2]
    for sublist in zip_codes:
        if sublist[0] == zip_code1:
            not_found_codes.remove(zip_code1)
            coord1 = [sublist[1], sublist[2]]
        elif sublist[0] == zip_code2:
            not_found_codes.remove(zip_code2)
            coord2 = [sublist[1], sublist[2]]
    if len(not_found_codes) == 0:
        dist = coord_distance(coord1[0], coord1[1], coord2[0], coord2[1])
        print('The distance between', zip_code1, 'and', zip_code2, 'is {:5.2f}'.format(dist), 'miles')
    else:
        print('Code(s)', ", ".join(map(str, not_found_codes)), 'not found')


while True:
    com = input("Command('loc', 'zip', 'dist', 'end') => ")
    com = com.lower()
    if com == 'loc':
        loc_fun()
    elif com == 'zip':
        zip_fun()
    elif com == 'dist':
        dist_fun()
    elif com == 'end':
        print('Done')
        break
    else:
        print('Invalid command, ignoring')
