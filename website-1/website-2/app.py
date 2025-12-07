from flask import Flask
app2=Flask(__name__)

@app2.route('/')
def home():
    return "welcome to the Website 2!"
@app2.route('/about')
def about():
    return "this is the about page of website 2."
@app2.route('/contact')
def contact():
    return " this is the contact@website2.com"
@app2.route('/blog')
def blog():
    return "this is the "
if __name__=='__main__':
    app2.run(debug=True)