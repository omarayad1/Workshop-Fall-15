from flask import Flask, jsonify,render_template,request
app = Flask(__name__)
app.config['DEBUG'] = True
global users
global ids
users = [{"name": "Mr Watermelon", "username": "batee5_92", "id": 1},
{"name": "Mrs Watermelon", "username": "batee5a_95", "id": 2}]
ids=2
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users',methods=['GET','POST'])
def users_data():
	if request.method == "GET":
		return jsonify({"data":users})
	elif request.method == "POST":
		global ids
		ids+=1
		users.append({"name": request.values['name'],"username": request.values['username'],"id": ids})
		return jsonify({"msg":"ok"})

@app.route('/users/<int:id>',methods=['PUT',"DELETE","GET"])
def single_user(id):
	if request.method == 'PUT':
		for i in xrange(len(users)):
			if users[i]['id'] == id:
				users[i]['name'] = request.values['name']
				users[i]['username'] = request.values['username']
				break
		return jsonify({'msg':'updated'})
	elif request.method == "DELETE":
		for i in xrange(len(users)):
			if users[i]['id'] == id:
				del users[i]
				break
		return jsonify({'msg':'deleted'})
	elif request.method == "GET":
		for i in lenusers:
			if el['id'] == id:
				return jsonify(el)
if __name__ == '__main__':
    app.run()