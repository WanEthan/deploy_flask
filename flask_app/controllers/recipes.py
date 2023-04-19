from flask_app import app, render_template, session, redirect, request
from flask_app.models.recipe import Recipe

# ***------------------------ Read All Recipes --------------------------***

@app.route("/recipes")
def dashbaord():
    if 'user_id' in session:
        recipes = Recipe.get_all()
        print(recipes)
        return render_template('recipes/index.html', recipes=recipes)
    return redirect('/')

# ***------------------------ Read One Recipe --------------------------***

#! READ ONE
@app.route('/recipes/show/<int:id>')
def show(id):
    if 'user_id' in session:
        recipe = Recipe.get_recipe(id)
        print(recipe)
        return render_template('recipes/show.html', recipe = recipe)
    return redirect('/')

# ***------------------------ CREATE --------------------------***


@app.route("/new")
def create_new_user():
    if 'user_id' in session:
        return render_template("recipes/new.html")
    return redirect('/')

@app.route('/create', methods=['post'])
def new_recipe():
    print(request.form)
    # TODO validate user
    if not Recipe.validate_recipe(request.form):
        return redirect('/new')
    Recipe.save(request.form)
    return redirect("/recipes")

# ***------------------------ UPDATE --------------------------***

@app.route('/recipes/update/<int:id>')
def edit_recipe(id):
    if 'user_id' in session:
        return render_template('recipes/edit.html', recipe = Recipe.get_recipe(id))
    return redirect('/')

@app.route('/update', methods=['post'])
def update_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/update/{request.form['id']}")
    Recipe.update(request.form)
    return redirect('/recipes')


# ***------------------------ DELETE --------------------------***

@app.route('/recipes/delete/<int:id>')
def destroy(id):
    Recipe.delete(id)
    return redirect('/recipes')


# ***------------------------ Return --------------------------***


@app.route('/back')
def return_recipes():
    return redirect('/recipes')