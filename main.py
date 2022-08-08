#from crypt import methods
#import flask
from flask import Flask,redirect ,url_for,render_template,request
#from requests import request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    result_dict = {
        'score' : score,
        'status' : 'PASSED'
    }
    return render_template('result.html',dict_passer = result_dict)

@app.route('/fail/<int:score>')
def fail(score):
    result_dict = {
        'score' : score,
        'status' : 'FAILED'
    }
    return render_template('result.html' , dict_passer = result_dict)

@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks > 50:
        result = 'success'
    else:
        result = 'fail'

    return redirect(url_for(result,score=marks)) 

@app.route('/submit',methods=['GET','POST'])
def submit():

    total_score = 0
    if request.method == 'POST':

        science =  float(request.form['science'])
        maths =  float(request.form['maths'])
        c =  float(request.form['c'])
        data_science =  float(request.form['data_science'])

        total_score  = (science+maths +c +data_science)/4

    res=''
    if total_score >= 50:
        res ='success'
    else:
        res ='fail'

    return redirect(url_for(res , score = total_score)) # passing total_score to the success/fail argument

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=9696)
    #app.run(debug=True, host='127.0.0.1', port=9696)