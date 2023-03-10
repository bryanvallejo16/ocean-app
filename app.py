from flask import Flask
from keplergl import KeplerGl

#map
m = KeplerGl()


#app

app = Flask(__name__)

@app.route('/',  methods=['GET'])
def index():
    return m._repr_html_()
    
if __name__ == '__main__':
    app.run(debug=True, 
            port=8080, 
            host='0.0.0.0')