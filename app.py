from flask import Flask,make_response,jsonify,render_template
import os

app=Flask(__name__, instance_relative_config=True)


@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, port=41005)