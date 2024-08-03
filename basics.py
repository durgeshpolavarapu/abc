from flask import Flask, render_template, request
import pickle # not in basic
import numpy as np # not in basic

model = pickle.load(open('iri.pkl', 'rb')) # not in basic

app = Flask(__name__)


@app.route('/home1')
def home(): # (basic) make fn name as home by default
    return render_template('home.html')


@app.route('/predict', methods=['POST']) # not in basic
def man():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)





