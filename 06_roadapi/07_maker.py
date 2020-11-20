from flask import Flask
import folium
import pandas as pd

import folium

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

@app.route('/marker')
def marker():
    df = pd.read_csv('address3.csv')
    df['icon'] = ['map-marker', 'cloud', 'gift', 'info-sign', 'ok-circle']
    color_dict = {'Clear': 'blue', 'Snow': 'white', 'Rain': 'gray', 'Extreme': 'red', 'Clouds': 'orange', 'Mist': 'green'}
    mapping = folium.Map(location=[df.lat.mean(), df.lng.mean()], zoom_start=12)
    for i in df.index:
        folium.Marker(
            location=[df.lat[i], df.lng[i]],
            popup=df['장소명'][i], 
            tooltip=f'{df.desc[i]}, {df.temp[i]}',
            icon=folium.Icon(color=color_dict[df.weather[i]], icon=df.icon[i])
        ).add_to(mapping)
    return mapping._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)