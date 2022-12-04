from flask import Flask, render_template
import glob
import yaml 

app = Flask(__name__)

def get_recipes():
  # read yaml
  recipes = []
  for item in list(glob.glob('./static/data/*.yml')):
    with open(item, 'r') as stream:
      recipe = yaml.safe_load(stream)
      path = item.replace('./static/data/','recipes/')
      recipe['path'] = path.replace('.yml','')  
      recipes.append(recipe)
  print(recipes)
  return recipes

def get_recipe(name):
  path = './static/data/' +  name + '.yml'
  with open(path, 'r') as stream:
    recipe = yaml.safe_load(stream)
    print(recipe)
    return recipe

@app.route('/')
def index():
  recipes = get_recipes()
  return render_template('index.html', recipes=recipes)

@app.route('/recipes/<name>')
def recipes(name):
  recipe = get_recipe(name)
  return render_template('recipe.html', recipe=recipe)