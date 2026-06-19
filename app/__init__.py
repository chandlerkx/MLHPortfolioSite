import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

pages = [
    {"name": "Home", "url": "/"},
    {"name": "Hobbies", "url": "/hobbies"}
]

hobbies = [
    {"name": "Hiking", "description": "Love exploring trails and getting summit views."},
    {"name": "Gaming", "description": "Currently grinding ranked in Valorant."},
    {"name": "Cooking", "description": "My specialty is stir fry but getting into baking."}
]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), pages=pages)


@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html', title="My Hobbies", hobbies=hobbies, pages=pages)

