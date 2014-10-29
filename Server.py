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

@route('/register')
def register():
    return '''
        <form action="/register" method="post">
            Name: <input name="new_name" type="text" />
            First name: <input name="new_firstName" type="text" />
            Choose username: <input name="new_username" type="text" />
            Choose pwd: <input name="new_password" type="password">
            <input value="Create account" type="submit">
    '''
@route('/register', method='POST')
def create_account():
    global documentJson
    global s_db_name
    new_name = request.forms.get('new_name')
    new_firstName = request.forms.get('new_firstName')
    new_username = request.forms.get('new_username')
    new_password = request.forms.get('new_password')

    js_users = documentJson['users']
    js_users.append({'id' : str(len(js_users)), 'firstName': new_firstName, 'lastName' : new_name, 'username': new_username, 'password' : new_password})

    f = open(s_db_name, 'w')
    f.write(json.dumps(documentJson, f))
    '''
    js_users = documentJson['users']
    js_users[len(js_users)]['id'] = str(len(js_users))
    js_users[len(js_users)]['firstName'] = new_firstName
    js_users[len(js_users)]['lastName'] = new_name
    js_users[len(js_users)]['username'] = new_username
    js_users[len(js_users)]['password'] = new_password
    '''
    return "<p>Created account with username "+ new_username+" :) </p>"

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



f = open('documentDB.txt', 'r+')#open document DB
global documentJson
documentJson = json.loads(f.read())
global s_db_name
s_db_name = 'documentDB.txt'

print documentJson
run(host='localhost', port=8080)






