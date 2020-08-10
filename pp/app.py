from flask import Flask,render_template,request
import pickle
import numpy as np
model = pickle.load(open('foodibm.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")
@app.route('/index.html')
def home1():
    return render_template(r"file:///C:/Users/HP/Desktop/pp/templates/index.html")

@app.route('/login',methods =['POST'])
def login():
    domain = 0
    sc = request.form['sc']
    bvc = request.form['bvc']
    bshhc = request.form['bshhc']
    ic = request.form['ic']
    mc= request.form['mc']
    
    print(ic)
    if(ic==6061 or ic == 6062):
        o1,o2,o3,o4,o5 = 0,0,1,0,0
        unit = "LCU/person/day"
    elif(ic==6063):
        o1,o2,o3,o4,o5 = 0,0,0,0,1
        unit = "kcal/capita/day"
    elif(ic==6064 or ic==6066 or ic==6065):
        o1,o2,o3,o4,o5 = 0,0,0,1,0
        unit = "g/capita/day"
    elif(int(ic)>=6067 and int(ic)<=6074 ):
        o1,o2,o3,o4,o5 = 1,0,0,0,0
        unit = "percent"
    else:
        o1,o2,o3,o4,o5 = 0,1,0,0,0
        unit = "LCU/1000 kcal"
    print(o1,o2,o3,o4,o5)
    
        
    
    
        
    total = [[o1,o2,o3,o4,o5,domain,int(sc),int(bvc),int(bshhc),int(ic),int(mc)]]
    print(total)
    y_pred = model.predict(total)
    y_pred=str(y_pred[0])+" "+unit
    print(y_pred)
    
    
    return render_template("main.html",showcase = y_pred)
    


if __name__ == '__main__':
    app.run(debug = True)
