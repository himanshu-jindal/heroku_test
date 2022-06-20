from flask import Flask

#flask object
app = Flask(__name__)



@app.route('/')
def index():
    return "hello himanshu jindal, deployed on herokuuuuuuu!"


if __name__ == '__main__':
    app.run()
