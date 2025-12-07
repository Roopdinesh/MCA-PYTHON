from flask import Flask

app4=Flask(__name__)
#temporary storage

products={
    1:{
        'name'='hp laptop'
        'price'=50000
    }
    1:{
        'name'='dell'
        'price'=40000
    }
}

@app4.route('/')
def home():
    return "Welcome to the laptop store"
if __name__=='__main__':
    @app4.run(debug=True)