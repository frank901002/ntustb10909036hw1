from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()  

@app.route("/readme")
def readme():
    return "This is ream me page. Please read me first!!"    

if __name__ == '__main__':
    app.run()  

