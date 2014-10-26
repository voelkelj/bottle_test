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
    loginRequest = check_login(username, password)
    if loginRequest[0]:
    	print 'check_login is true'
    	userJson = loginRequest[1]
        return "<p>Your login information was correct.</p><p>Welcome "+ userJson["firstName"]+ " "+ userJson["lastName"] + "</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(usr, pwd):
	#global loginJson
	global documentJson
	loginJson = documentJson
	usersJson = loginJson["users"]
	for user in usersJson:
		print "in for"
		username = user["username"]
		password = user["password"]
		if usr == username and pwd == password:
			return (True, user)
	return (False, None)



f = open('documentDB.txt')#open document DB
global documentJson
documentJson = json.loads(f.read())
print documentJson
run(host='localhost', port=8080)






