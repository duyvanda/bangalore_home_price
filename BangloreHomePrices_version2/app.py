from flask import Flask,redirect,url_for, render_template, request, session,flash
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))
dictionary={'1st Block Jayanagar':3,'Tuesday':2,'Wednesday':8,'Thursday':7,'Friday':5,'Saturday':6,'Sunday':7}
def loc_index(date):
    return dictionary.get(date)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])


def predict():
	int_features = []
	for x in request.form.values():
		int_features.append(x)
	area_sf = int(int_features[0])
	bhk = int(int_features[1])
	bath = int(int_features[2])
	location = int_features[3]

	a = np.zeros(243)
	a[0] = area_sf
	a[1] = bhk
	a[2] = bath
	a[loc_index(location)] = 1
	prediction = model.predict([a])
	output = round(prediction[0], 2)
	return render_template('index.html', text='bangalore home price should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)