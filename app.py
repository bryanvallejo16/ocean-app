from flask import Flask
from keplergl import KeplerGl
import geopandas as gpd

#read
data = gpd.read_file('data/azores_whales_records.gpkg', driver='GPKG')

data['timestamp'] = data['timestamp'].astype(str)

#map
m = KeplerGl()


#app

app = Flask(__name__)

@app.route('/',  methods=['GET'])
def index():
    return m._repr_html_(data = {'wildlife':data})
    
if __name__ == '__main__':
    app.run(debug=True, 
            port=8080, 
            host='0.0.0.0')