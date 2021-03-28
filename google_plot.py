import requests

def main(start, end):
    API = 'AIzaSyCWmcq5BfF4LFha5ZufuEO27ixsl3OpBjs'
    directions_link = "https://maps.googleapis.com/maps/api/directions/json?"
    #start = find_loc(start, API)
    #end = find_loc(end, API)

    get_route(start, end, API=API, directions_link=directions_link)



def find_loc(name, API):
    modified_name = '+'.join(name.replace(',', '').split(sep=' '))
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={modified_name}&key={API}')
    resp_json_payload = response.json()
    lat = resp_json_payload['results'][0]['geometry']['location']['lat']
    lng = resp_json_payload['results'][0]['geometry']['location']['lng']

    return lat, lng


def get_route(start, end, API, directions_link):
    start = find_loc(start, API)
    end = find_loc(end, API)
    print(start, end)
    response = requests.get(directions_link +f'origin={start[0]},{start[1]}&destination={end[0]},{end[1]}&key={API}&mode=driving')
    resp_json_payload = response.json()
    #print(resp_json_payload)
    coords = []

    for dot in resp_json_payload['routes'][0]['legs'][0]['steps']:
        lat_end = dot['end_location']['lat']
        lng_end = dot['end_location']['lng']
        lat_start = dot['start_location']['lat']
        lng_start = dot['start_location']['lng']
        coords.append((lat_end, lng_end))
        coords.append((lat_start, lng_start))

    return coords

main('Ashok Gardens, Mumbai', 'High Street Phoenix, Mumbai')



# https://maps.googleapis.com/maps/api/directions/json?origin=18.9953464,72.848134&destination=18.994744,72.82459930000002&key=AIzaSyCWmcq5BfF4LFha5ZufuEO27ixsl3OpBjs&mode=driving