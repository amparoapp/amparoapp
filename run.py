from flask import Flask,make_response,jsonify,render_template

app=Flask(__name__, instance_relative_config=True)


@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)