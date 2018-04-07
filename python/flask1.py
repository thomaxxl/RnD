# curl -X POST 127.0.0.1:5000?a=b -d 'x=y'
from flask import Flask, request
app = Flask(__name__)
 
@app.route('/', methods=['POST', 'GET'])
def test():
    return 'request.args: {} , request.form: {}'.format(request.args ,request.form)
 
app.run()

