from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def info():
    outstr =  '<pre>'
    for key in os.environ.keys():
        outstr += "%50s %s \n" % (key,os.environ[key])
    return outstr + '</pre>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
