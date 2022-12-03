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
      recipe['path'] = item.replace('./static/data/','recipes/')
      recipes.append(recipe)
  print(recipes)
  return recipes

@app.route('/')
def index():
  recipes = get_recipes()
  return render_template('index.html', recipes=recipes)