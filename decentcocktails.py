from flask import Flask, render_template, url_for
import logging
import os
import json

app = Flask(__name__)
logging.basicConfig(filename = 'flask.log', level=logging.DEBUG, format = f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


class Recipe:
	def __init__(self, recipe):
		self.name = recipe['name']
		self.pageName = recipe['name'].replace(' ', '-').lower()
		self.description = recipe['description']
		self.ingredients = recipe['ingredients']
		self.instructions = recipe['instructions']

	def __getitem__(self, item):
		return getattr(self, item)

def get_recipe(recipes, pageName):
	# next(item for item in dicts if item["name"] == "Pam")
	app.logger.debug("searching recipes")
	recipe = next(recipe for recipe in recipes if recipe["pageName"] == pageName)
	if recipe:
		return recipe
	return None

def load_recipes():
	recipes = []
	path = "./static/data/"
	try:
		for filename in [file for file in os.listdir(path) if file.endswith(".json")]:
			app.logger.debug(filename)
			with open(path + filename) as jsonFile:
				app.logger.debug("Loading, ", jsonFile)
				data = json.load(jsonFile)
				recipes.append(Recipe(data))
	except:
		app.logger.debug("Failed to load recipes")
	return recipes

@app.route('/')
@app.route('/index')
def index():
	recipes = load_recipes()
	return render_template('index.html', recipes=recipes)

@app.route('/<recipeName>')
def recipe_page(recipeName):
	app.logger.debug("building page for %s", recipeName)
	recipes = load_recipes()
	recipe = get_recipe(recipes, recipeName)
	if recipe:
		app.logger.debug("found a recipe for %s, building page", recipeName)
		return render_template('recipe.html', recipe=recipe)
	else:
		errorMessage = "page not found: " + recipe
		return render_template('error.html', error='404', text=errorMessage), 404


@app.errorhandler(404)
def page_not_found(e):
	print('404', e)
	return render_template('error.html', error='404', text=e), 404

@app.errorhandler(500)
def error_500(e):
	print('500', e)
	return render_template('error.html', error='500', text=e), 500

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


