
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/calc',methods=['post'])
def calc():
    num1=request.form['a']
    num2=request.form['b']
    if 'add' in request.form:
        ans=int(num1)+int(num2)
    elif 'sub' in  request.form:
        ans=int(num1)-int(num2)
    else:
        ans='invalid'
        return render_template('index.html',result=ans)
        
    pass
if __name__=='__main__':
    app.run(debug=True)