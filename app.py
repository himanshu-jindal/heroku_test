from flask import Flask

#flask object
app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return "hello himanshu, deployed on herokuuuuuuu!"


if __name__ == '__main__':
    app.run()
