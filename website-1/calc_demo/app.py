from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/calc',methods=['get','post'])
def calc():
    result=None
    if request.method=='post':
        num1=float(request.form['num1'])
        num2=float(request.form['num2'])
        result=num1+num2
        return render_template('calc.html',result=result)
        
    pass
if __name__=='__main__':
    app.run(debug=True)