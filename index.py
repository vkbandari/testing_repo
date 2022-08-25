from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Deployment success'


if __name__ == '__main__':
    app.run(host='localhost', port= 5000, debug = True)
