from flask import Flask,request,render_template
import pickle

app = Flask(__name__)

with open('diabetes_std.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('diabetes_knn.pkl', 'rb') as file:
     knn = pickle.load(file)

@app.route('/', methods =["GET", "POST"])
def home():

    return render_template("home.html")


@app.route('/pred', methods =["GET", "POST"])
def pred():
    if request.method == "POST":
        x1 =  request.form.get('x1')
        x2 =  request.form.get('x2')
        x3 =  request.form.get('x3')
        x4 =  request.form.get('x4')
        x5 =  request.form.get('x5')
        x6 =  request.form.get('x6')
        x7 =  request.form.get('x7')
        x8 =  request.form.get('x8')

        print(x1,x2,x3,x4,x5,x6,x7,x8)
        l = [float(x1),float(x2),float(x3),float(x4),float(x5),float(x6),float(x7),float(x8)]
        l = scaler.transform([l])
        out = knn.predict(l)
        print(out)
        if out[0] == 0:
            pred = "Normal"
        else :
            pred = "Diabetic"




        return render_template("pred.html",pred = pred)
    return render_template("pred.html",pred = False)


if __name__ == '__main__':
    app.run(debug=True)
