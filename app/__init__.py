import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

photos = ["IMG_2488.jpg", "IMG_2493.jpg", "IMG_2402.jpg"]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), photos=photos)

