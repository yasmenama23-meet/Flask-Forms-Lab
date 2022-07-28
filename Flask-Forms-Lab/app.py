from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "meana22"
password = "2006"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		user = request.form['username']
		userpass  = request.form['password']
		if username==user and userpass==password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])  
def home():
	return render_template('home.html', f=facebook_friends)

@app.route('/friend_exists/<string:name>',methods=['GET', 'POST'])
def hello_name_route(name):
    return render_template(
        'friend_exists.html', name= name in facebook_friends )


  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)