from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.rpute("/<name>")
@app.route("/home/")
@app.route("/about/")
def home(name=None):
	return render_template('home.html', name=name)

@app.route("/countries/")
def countries():
	return render_template('countries.html')

@app.route("/contact/")
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)