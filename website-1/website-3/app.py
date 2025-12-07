from flask import Flask

app3=Flask(__name__)

@app3.route('/user/<username>')
def show_user(username):
    return f"👤 User profile :{username}"

@app3.route('/post<int:post_id>')
def show_post(post_id):
    return f" "

if __name__=='__main__':
    app3.run(debug=True)