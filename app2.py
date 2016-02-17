from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/<name>/<int:answer>')
def guess(name, answer):
	correct = (answer == 42)
	return render_template(
		'guess.html',
		name=name,
		correct=correct
	)

if __name__ == '__main__':
	app.run(debug=True)
