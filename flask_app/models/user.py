from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
import re
# the regex module
# create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

DATABASE = 'uers_recipes'

class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ***------------------------Save data to Database--------------------------***

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return User(result[0])


# ***------------------------Validate inputs--------------------------***

    @staticmethod
    def validate_user(user):
        print(user)
        is_valid = True
        # First Name - letters only, at least 2 characters and that it was submitted
        if len(user['first_name']) < 2 or not user['first_name'].isalpha():
            is_valid = False
            flash("First name must be letters only and at least 2 chars")

        # Last Name - letters only, at least 2 characters and that it was submitted
        if len(user['last_name']) < 2 or not user['last_name'].isalpha():
            is_valid = False
            flash("Last name must be letters only and at least 2 chars")

        # Email - valid Email format, does not already exist in the database, and that it was submitted
        email_check = {'email': user['email']}
        if User.get_by_email(email_check):
            flash("Email address already exists!")
            is_valid = False

        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False

        # Password - at least 8 characters, and that it was submitted
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 chars")

        # Password Confirmation - matches password
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash("passwords must match")
        
        return is_valid