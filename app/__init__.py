import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

hobbies = [
    {
        "name": "Hiking",
        "image": "hiking.png",
        "description": "Love getting outside and exploring trails whenever I can. Nothing beats a good summit view."
    },
    {
        "name": "Gaming",
        "image": "gaming.png",
        "description": "Big into both competitive and chill games. Currently grinding ranked in Valorant."
    },
    {
        "name": "Cooking",
        "image": "cooking.png",
        "description": "Always trying to learn new recipes. My specialty is stir fry but I'm getting into baking too."
    }
]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), hobbies=hobbies)

