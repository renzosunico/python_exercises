from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)

@app.route('/')
def home():
	
	return render_template(
		'home.html'
	)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		session['username'] = request.form['username']
		session['password'] = request.form['password']
		return render_template('okay.html')

app.secret_key = 'saldjsakldjlaskdjaskjdelqwirhjekjrnfemnfklsdefes53r4esdfsdf5sd4f56f4e55'
if __name__ == '__main__':
	app.run(debug=True)
