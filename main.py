from flask import Flask, request, jsonify,render_template
from flask_cors import cross_origin
import pickle

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/App',methods=['POST','GET'])
@cross_origin()
def page():
    if request.method == 'POST':
        try:
            CRIM = float(request.form['CRIM'])
            ZN = float(request.form['ZN'])
            CHAS = float(request.form['CHAS'])
            LSTAT = float(request.form['LSTAT'])
            # load file
            filename = 'final_model.pickle'
            load_file = pickle.load(open(filename, 'rb'))

            Prediction = load_file.predict([[CRIM, ZN, CHAS, LSTAT]])

            return render_template('results.html',Prediction=Prediction[0])
        except Exception as e:
            print('The Exception message is: ', e)
            return jsonify('error: Something is wrong')




@app.route('/post_man',methods=['POST'])
def post():
    if request.method == 'POST':
        CRIM = float(request.json['CRIM'])
        ZN = float(request.json['ZN'])
        CHAS = float(request.json['CHAS'])
        LSTAT = float(request.json['LSTAT'])

        #load file
        filename = 'final_model.pickle'
        load_file = pickle.load(open(filename,'rb'))

        predction = load_file.predict([[CRIM,ZN,CHAS,LSTAT]])
        result = predction[0]
        return jsonify(result)


if __name__ =='__main__':
    app.run()