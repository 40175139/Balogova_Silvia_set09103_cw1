from flask import Flask, render_template, redirect, url_for, abort
import json

app = Flask(__name__)


json_file = open("country_data.json").read()
country_list = json.loads(json_file)



@app.route("/")
@app.route("/home/")
@app.route("/about/")
def home(name=None):
	return render_template('about.html', name=name)

@app.route("/countries/")
def countries():
	countries = sort_by_continent(country_list)
	return render_template('countries.html', countries=countries)

@app.route("/contact/")
def contact():
	return render_template('contact.html')


# The dictionary of countries
@app.route("/countries/<name>")
def country_detail(name):
	for country in country_list:
		if country["name"].lower() == name.lower():
			return render_template('countries_detail.html', country=country)
	return "Not loading country detail."
	#abort(404)


@app.errorhandler(404)
def error_404(error):
	return render_template('error.html'), 404

def sort_by_continent(list):
	continents = { }

	for country in country_list:
		continent = country["continent"]

		if continent not in continents:
			continents[continent] = []

		continents[continent].append(country)

	return continents

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
