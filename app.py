from flask import Flask
from keplergl import KeplerGl
import geopandas as gpd

#read
data = gpd.read_file('data/azores_whales_records.gpkg', driver='GPKG')

data['timestamp'] = data['timestamp'].astype(str)

# fetch
data = data.loc[data['wild_id'].isin([ 'wt-72315722'])] # 'wt-72315732',


config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "Great Whales"
          ],
          "id": "hflv90e0g",
          "name": [
            "timestamp"
          ],
          "type": "timeRange",
          "value": [
            1211810400000,
            1222923509000.0002
          ],
          "enlarged": True,
          "plotType": "histogram",
          "animationWindow": "free",
          "yAxis": None
        }
      ],
      "layers": [
        {
          "id": "cm7q9ak",
          "type": "geojson",
          "config": {
            "dataId": "Great Whales",
            "label": "Great Whales",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": None,
              "colorRange": {
                "name": "ColorBrewer Paired-8",
                "type": "qualitative",
                "category": "ColorBrewer",
                "colors": [
                  "#a6cee3",
                  "#1f78b4",
                  "#b2df8a",
                  "#33a02c",
                  "#fb9a99",
                  "#e31a1c",
                  "#fdbf6f",
                  "#ff7f00"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "wild_id",
              "type": "string"
            },
            "colorScale": "ordinal",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "lbhpz34",
          "type": "grid",
          "config": {
            "dataId": "Phytoplankton",
            "label": "Point",
            "color": [
              221,
              178,
              124
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.6,
              "worldUnitSize": 30,
              "colorRange": {
                "name": "ColorBrewer Greens-9",
                "type": "singlehue",
                "category": "ColorBrewer",
                "colors": [
                  "#f7fcf5",
                  "#e5f5e0",
                  "#c7e9c0",
                  "#a1d99b",
                  "#74c476",
                  "#41ab5d",
                  "#238b45",
                  "#006d2c",
                  "#00441b"
                ]
              },
              "coverage": 1,
              "sizeRange": [
                0,
                500
              ],
              "percentile": [
                0,
                100
              ],
              "elevationPercentile": [
                0,
                100
              ],
              "elevationScale": 5,
              "colorAggregation": "average",
              "sizeAggregation": "count",
              "enable3d": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "CHLa_mg_L",
              "type": "real"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "Great Whales": [
              {
                "name": "timestamp",
                "format": None
              },
              {
                "name": "location_long",
                "format": None
              },
              {
                "name": "individual_id",
                "format": None
              },
              {
                "name": "tag_id",
                "format": None
              },
              {
                "name": "wild_id",
                "format": None
              }
            ],
            "Phytoplankton": [
              {
                "name": "time",
                "format": None
              },
              {
                "name": "depth",
                "format": None
              },
              {
                "name": "CHLa_mg_L",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 39.08282277285858,
      "longitude": -47.56469878817516,
      "pitch": 0,
      "zoom": 1.7759365278629409,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "satellite",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}
#map
m = KeplerGl()


#app

app = Flask(__name__)

@app.route('/',  methods=['GET'])
def index():
    return m._repr_html_(data = {'Great Whales':data}, config=config)
    
if __name__ == '__main__':
    app.run(debug=True, 
            port=8080, 
            host='0.0.0.0')