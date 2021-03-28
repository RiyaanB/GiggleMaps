from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from bokeh.io import show
from google_graph_writer import find_loc, get_data, get_routes

def plot_google_graph(start, end, API='AIzaSyCWmcq5BfF4LFha5ZufuEO27ixsl3OpBjs', directions_link="https://maps.googleapis.com/maps/api/directions/json?", zoom=12, map_type='roadmap'):
    try:
        start = find_loc(start, API)
        end = find_loc(end, API)
        data = get_data(start, end, API=API, directions_link=directions_link, alternatives='true')
        all_coords = get_routes(data) #Diff from google_graph_writer
    except Exception:
        raise RuntimeError('Error in getting data from Google Maps')

    bokeh_width, bokeh_height = 900,800
    
    all_lats = []
    all_lngs = []
    
    for coords in all_coords:
        lats = []
        lngs = []

        for lat, lng in coords:
            lats.append(lat)
            lngs.append(lng)
        
        all_lats.append(lat)
        all_lngs.append(lng)
    
    gmap_options = GMapOptions(lat=lats[0], lng=lngs[0], map_type=map_type, zoom=zoom)
    
    p = gmap(API, gmap_options, title='Route Map', width=bokeh_width, height=bokeh_height)
    colour_code = ['red', 'yellow', 'blue'] #Need to generalise

    for i in range(len(all_coords)):
        for lat, lng in all_coords[i]:
            center = p.circle([lng],[lat], size=10, alpha=0.5, color=colour_code[i])
    
    show(p)
    return p

if __name__ == '__main__':
    plot_google_graph('Four Seasons Hotel, Mumbai', 'Dhirubhai Ambani International School, Mumbai')