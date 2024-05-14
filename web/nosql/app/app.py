from flask import Flask, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.challenge
users = db.users

@app.route('/')
def index():
    with open(__file__, "r") as f:
        source_code = f.read()
    return source_code, 200, {'Content-Type': 'text/plain'}


@app.route('/login', methods=['GET'])
def login_form():
    return '''
    <form method="POST" action="/login">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password">
        <br>
        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = users.find_one({'username': username, 'password': password})

        if user:
            with open('flag.txt', "r") as f:
                flag = f.read()
            return f'Welcome\n{flag}', 200, {'Content-Type': 'text/plain'}
        else:
            return 'Invalid username or password'
    else:
        return 'Request must be in JSON format.'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=6002)
