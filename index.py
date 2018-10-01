from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
	return 'I am the main page'

@app.route("/chocolate/")
def chocolate():
	return 'I am the page about chocolate'

@app.route("/about/")
def about():
	return 'I am the page about about'

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
