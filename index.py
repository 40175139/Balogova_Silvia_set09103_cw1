from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def main(name=None):
	return render_template('home.html', name=name)

@app.route('/chocolate/')
def chocolate():
	return 'I am the page about chocolate'

@app.route('/about/')
def about():
	return 'I am the page about about'

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
