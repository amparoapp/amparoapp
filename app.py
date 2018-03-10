from flask import Flask,make_response,jsonify,render_template,request

app=Flask(__name__, instance_relative_config=True)


@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')


def post_login():
	pass

def get_login():
	return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
	print(request.method)
	if request.method == 'GET':
		get_login()
	else:
		post_login()

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)