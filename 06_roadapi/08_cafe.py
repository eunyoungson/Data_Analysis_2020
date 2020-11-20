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
    cafe = pd.read_csv('cafe.csv')
    mapping = folium.Map(location=[cafe['위도'].mean(), cafe['경도'].mean()], zoom_start=12)
    for i in cafe.index:
        #if cafe['지점명'][i] == 'NaN':
       # _tooltip =cafe['상호명'][i]
    #else:
        #_tooltip =cafe['지점명'][i]
        folium.Marker(
            location=[cafe['위도'][i], cafe['경도'][i]],
            popup = cafe['상호명'][i],
            #tooltip = _tooltip,
            tooltip =cafe['지점명'][i],
            icon=folium.Icon(color=cafe.color[i], icon=cafe.icon[i])
).add_to(mapping)
    return mapping._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)