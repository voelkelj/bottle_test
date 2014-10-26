from bottle import route, run, template, request
import json

loginJson = json.loads('{"users" : [{"id" : "1", "firstName" : "Julian", "lastName" : "Voelkel", "username" : "julian_voelkel@gmx.de", "password" : "12345678"}]}')

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/hello/<name>/mom')
def index(name):
	return template('<b>Hey {{name}}, your mama is fat</b>', name=name)

@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)
    return template('<b> Hello number {{id}}', id=id)


@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(usr, pwd):
	global loginJson
	username = loginJson["users"][0]["username"]
	password = loginJson["users"][0]["password"]
	return usr == username and pwd == password
	#return usr == 'julian_voelkel@gmx.de' and pwd == '75b5bd19'

run(host='localhost', port=8080)