from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# our index route will handle rendering our form
# set a secret key for security purposes
app.secret_key = "this is a secret string I want"

bcrypt = Bcrypt(app)