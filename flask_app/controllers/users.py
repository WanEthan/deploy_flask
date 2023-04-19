from flask_app import app, render_template, redirect, request, session, flash, bcrypt
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template("index.html")


# ***------------------------ CREATE --------------------------***

@app.route("/register", methods=['post'])
def register():
    print(request.form)

    # TODO validate user
    if not User.validate_user(request.form):
        return redirect('/')
    # create the hash for password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    # the save @classmethod will return user ID
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']

    return redirect('/recipes')

# ***------------------------ LogIn --------------------------***

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    password_valid = bcrypt.check_password_hash(user_in_db.password, request.form['password'])
    if not password_valid:
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    # never render on a post!!!
    return redirect('/recipes')

# ***------------------------ LogOut --------------------------***

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
