from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def info():
    outstr =  '<pre>'
    for key in sorted(os.environ.keys()):
        outstr += "%30s %s \n" % (key,os.environ[key])
    return outstr + '</pre>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
