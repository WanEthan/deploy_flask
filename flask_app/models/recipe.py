from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash

# the regex module
# create a regular expression object that we'll use later

DATABASE = 'uers_recipes'

class Recipe:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.cook_time = data['cook_time']
        self.user_id = data['user_id']
        self.user = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# ***------------------------Save data to Database--------------------------***

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date, cook_time, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(cook_time)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    

# ***------------------------Read All Recipes--------------------------***

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        recipes = []
        for recipe_dict in results:
            recipes.append(Recipe(recipe_dict))
        return recipes
    
# ***------------------------Read One Recipe--------------------------***
    @classmethod
    def get_recipe(cls, id):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        data = {'id': id}
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result[0])
        recipe = Recipe(result[0])
        return recipe
    
# ***------------------------UPDATE--------------------------***
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s,cook_time=%(cook_time)s, date=%(date)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
# ***------------------------ DELETE --------------------------***

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        data = {'id':id }
        return connectToMySQL(DATABASE).query_db(query, data)
    

# ***------------------------Validate inputs--------------------------***

    @staticmethod
    def validate_recipe(recipe):
        print(recipe)
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 chars")
        
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 chars")

        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 chars")
        
        if recipe['date'] == "":
            is_valid = False
            flash("Please select a date!")

        if 'cook_time' not in recipe:
            is_valid = False
            flash("Please select 'Yes' or 'No'!")
        
        return is_valid