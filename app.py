from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

def prediction(lst):
    filename='F:/Ai/web/model/mod.pkl'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value=model.predict([lst])
    return pred_value
    

@app.route('/', methods=['POST','GET'])
def index():
    pred = 0
    if request.method == 'POST':
        chloraphyll = request.form['Chlorophyll µg/L']
        temp = request.form['Temp °C']
        tds = request.form['TDS mg/L']
        depth = request.form['Depth m']
        pressure = request.form['pressure']
        
        feature_list = []
        feature_list.append(float(chloraphyll))
        feature_list.append(float(temp))
        feature_list.append(float(tds))
        feature_list.append(float(depth))
        feature_list.append(float(pressure))
        
        pred = prediction(feature_list)
        print(pred)
        
    return render_template('index.html', pred=pred)

if __name__ =='__main__':
    app.run(debug=True)