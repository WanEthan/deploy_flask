# checklist

- [x] create a new directory
- [ ] inside the directory create virtural env by running:

```bash
[python -m] pipenv install flask pymysql flask-bcrypt
```

- [ ] activate the virtual env every time you open a new terminal:

```bash
[python -m] pipenv shell 
```
## modularized app
- [ ] create [server.py](server.py)

# make `flask_app`

- [ ] [`models`](flask_app/models/user.py)
- [ ] [`config`](flask_app/config/mysqlconnection.py)
- [ ] [`controllers`](flask_app/controllers/users.py)
- [ ] [`templates`](flask_app/templates/index.html)
- [ ] [`static`](flask_app/static/css/style.css)

- [ ] [`__init__.py`](flask_app/__init__.py)
```py
from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')  # Return the string 'Hello World!' as a response
## MORE ROUTES HERE 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
```

- [ ] start application by running:

```
python server.py
```

- [ ] go to [localhost:5000](http://localhost:5000/)

- [ ] create a [templates](templates/index.html) folder that contains our HTML