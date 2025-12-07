from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['get','post'])

def index():
    errors=''
    if request.method=='post':
        uname=request.form['username']
        email=request.form['email']
        pwd=request.form['pwd']
        pwd2=request.form['pwd2']
        if len(uname)<2 or len(email)< 10 or pwd!=pwd2:
            error='invalid detials'
            
        else:
            return render_template('output.html',username=uname,email=email)
        return render_template('index.html',errors=error)
    
if __name__=='__main__':
    app.run(debug=True)