from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route("/readme")
def readme():
    return "This is ream me page. Please read me first!!"    

@app.route("/newPage")
def newPage():
    return "This is new page!" 

if __name__ == '__main__':
    app.run()  

