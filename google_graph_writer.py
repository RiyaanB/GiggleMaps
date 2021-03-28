import requests

def write_google_graph(start, end, API='AIzaSyCWmcq5BfF4LFha5ZufuEO27ixsl3OpBjs', directions_link="https://maps.googleapis.com/maps/api/directions/json?"):   
    try:
        start = find_loc(start, API)
        end = find_loc(end, API)
        data = get_data(start, end, API=API, directions_link=directions_link, alternatives='true')
        times = get_time(data)
        routes = get_routes(data)
    except Exception:
        raise RuntimeError('Error in getting data from Google Maps')

    
    fictional_points = [(end[0]+i*1e-6, end[1]+i*1e-6) for i in range(1, len(times) + 1)]

    with open('Google_graph.txt', 'w') as w:
        modified_start = modify_coord(start)
        modified_end = modify_coord(end)

        for i in range(len(times)):
            modified_fictional = modify_coord(fictional_points[i])
            w.write(','.join( [modified_start, modified_fictional, str(times[i]) ] ) + '\n')
            w.write(','.join( [modified_fictional, modified_end, '1' ] ) + '\n')

def modify_coord(coords):
    coords = (str(coord) for coord in coords)
    return '_'.join(coords)

def find_loc(name, API):
    modified_name = '+'.join(name.replace(',', '').split(sep=' '))
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={modified_name}&key={API}')
    resp_json_payload = response.json()
    lat = resp_json_payload['results'][0]['geometry']['location']['lat']
    lng = resp_json_payload['results'][0]['geometry']['location']['lng']

    return lat, lng

def get_data(start, end, API, directions_link, alternatives='false'):
    link = directions_link + f'origin={start[0]},{start[1]}&destination={end[0]},{end[1]}&key={API}&mode=driving&alternatives={alternatives}'
    #print(link)
    response = requests.get(link)
    resp_json_payload = response.json()

    return resp_json_payload

def get_time(resp_json_payload):
    return [route['legs'][0]['duration']['value'] for route in resp_json_payload['routes']]
        

def get_routes(resp_json_payload):
    all_coords = []
    for i in range(len(resp_json_payload['routes'])):
        path_coords = []
        for dot in resp_json_payload['routes'][i]['legs'][0]['steps']:
            lat_end = dot['end_location']['lat']
            lng_end = dot['end_location']['lng']
            lat_start = dot['start_location']['lat']
            lng_start = dot['start_location']['lng']
            path_coords.append((lat_end, lng_end))
            path_coords.append((lat_start, lng_start))
        
        all_coords.append(path_coords)
        
    return all_coords


write_google_graph('Ashok Gardens, Mumbai', 'Dhirubhai Ambani International School, Mumbai')



# https://maps.googleapis.com/maps/api/directions/json?origin=18.9953464,72.848134&destination=18.994744,72.82459930000002&key=AIzaSyCWmcq5BfF4LFha5ZufuEO27ixsl3OpBjs&mode=driving

'''
    r = set(coord for coord in routes[0])
    r1 = set(coord for coord in routes[1])
    r2 = set(coord for coord in routes[2])

    r3 = r.union(r1).union(r2)

    print(len(r3))
    exit()
    r = set()
    for route in routes:
        for coord in route:
            r.add(str(coord))
        print(len(r))

    print(len(r))

    for route in routes:
        print(len(route))

    exit()
    '''

#&departure_time=now&traffic_model=pessimistic