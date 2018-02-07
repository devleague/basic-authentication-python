from flask import Flask, request, Response
from functools import wraps
app = Flask(__name__)

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    return Response(
        'Could not verify access. Must use proper credentials',
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/login')
@requires_auth
def login():
    return render_template('login.html')

if __name__=='__main__':
    app.run(host = '10.0.1.72', port = 80)
