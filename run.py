from flask import Flask,make_response,jsonify,render_template,request

app=Flask(__name__, instance_relative_config=True)


@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	print(request.method)
	if request.method == 'GET':
		return render_template('login.html')
	else:
		if request.form and request.form['user'] and request.form['pass']:
			if request.form['user'] == "michael" and request.form['pass'] == "1234":
				return render_template("app.html")
			else:
				return render_template("login.html")
		else:
			return render_template("login.html")


@app.route('/app',methods=['GET'])
def amparoapp():
	return render_template('app.html')

@app.route('/app/avisos',methods=['GET'])
def amparoavisos():
	return render_template('avisos.html')

@app.route('/app/pacientes/francisco',methods=['GET'])
def paciente():
	return render_template('ejemplopaciente.html')
	
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)