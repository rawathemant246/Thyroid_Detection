from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler
import logging
import os

app = Flask(__name__)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
logging.basicConfig(filename='test.log', filemode='w+', format='%(asctime)s %(message)s')
lg = logging.getLogger()
lg.addHandler(c_handler)
open(os.getcwd() + 'test.log', 'a')

model = pickle.load(open('KNN_Model_gridserchCV.pkl', 'rb'))

@app.route('/',methods=['GET'])

def Home():
    try:
        return render_template('index.html')
    except Exception as E:
        lg.error(E)
        return render_template('error.html', message="check logs for more info")
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    try:
        if request.method =='POST':
            Age = request.form['Age']
            Sex = request.form['Sex']
            if (Sex=='Male'):
                Sex=1
            else:
                Sex =0
            onThyroxine = request.form['On Thyroxine']
            if (onThyroxine=='Yes'):
                onThyroxine=1
            else:
                onThyroxine=0
            QueryonThyroxine = request.form['QueryonThyroxine']
            if (QueryonThyroxine == 'Yes'):
                QueryonThyroxine =1
            else:
                QueryonThyroxine=0
            OnAntiThyroidMedication = request.form['OnAntiThyroidMedication']
            if (OnAntiThyroidMedication =='Yes'):
                OnAntiThyroidMedication =1
            else:
                OnAntiThyroidMedication =0
            Sick = request.form['Sick'] #np.log(kms_Driven
            if(Sick=='Yes'):
                Sick =1
            else:
                Sick=0
            Pregnant = request.form['Pregnant']
            if(Pregnant=='Yes'):
                Pregnant =1
            else:
                Pregnant=0
            ThyroidSurgery = request.form['ThyroidSurgery']
            if (ThyroidSurgery=='Yes'):
                ThyroidSurgery=1
            else:
                ThyroidSurgery=0
            I131_Treatment = request.form['I131_Treatment']
            if(I131_Treatment=='Yes'):
                I131_Treatment=1
            else:
                I131_Treatment=0
            QueryHypothyroid = request.form['QueryHypothyroid']
            if (QueryHypothyroid=='Yes'):
                QueryHypothyroid=1
            else:
                QueryHypothyroid=0
            Lithium = request.form['Lithium']
            if(Lithium=='Yes'):
                Lithium=1
            else:
                Lithium=0
            Goitre = request.form['Goitre']
            if(Goitre=='Yes'):
                Goitre=1
            else:
                Goitre=0
            Tumor = request.form['Tumor']
            if(Tumor=='Yes'):
               Tumor = 1
            else:
                Tumor =0
            Hypopitutitory = request.form['Hypopitutitory']
            if(Hypopitutitory=='Yes'):
                Hypopitutitory=1
            else:
                Hypopitutitory=0
            Psych =request.form['Psych']
            if (Psych=='Yes'):
                Psych=1
            else:
                Psych =0
            T3 = float(request.form['T3'])
            T4U = float(request.form['T4U'])
            ReferralSourceOther = float(request.form['ReferralSourceOther'])
            prediction = model.predict([[Age, Sex, OnThyroxine, QueryOnThyroxine, OnAntiThyroidMedication, Sick, Pregnant,
                                 ThyroidSurgery, I131_Treatment, QueryHypothyroid, QueryHyperthyroid, Lithium, Goitre,
                                 Tumor, Hypopituritory, Psych, T3, T4U, ReferralSourceOther]])
            print(prediction)
            output = round(prediction[0],2)
            print(output)
            if output==0:
                return render_template('index.html', prediction_text="Not having Thyroid")
            elif output ==1:
                return render_template('index.html', prediction_text = "Having Compensated Hypothyroid")
            elif output ==2:
                return render_template('index.html', predicition_text = "Having Primary Hypothyroid")
            else:
                return render_template('index.html', prediction_text= "Having Secondary Hypothyroid")
        else:
            return render_template('index.html')
    except Exception as E:
        lg.error(E)
        print("Exception Raise!! Kindly check the condition for Inputs Entered", E)

if __name__ == "__main__":
    app.run(debug=True)



