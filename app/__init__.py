import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

education = [
    {
        "school": "University of Placeholder",
        "degree": "B.S. Computer Science",
        "duration": "2022 - 2026",
        "description": "Focused on software engineering and systems. Involved in hackathons and the CS club."
    },
    {
        "school": "Community College",
        "degree": "Associate's in General Studies",
        "duration": "2020 - 2022",
        "description": "Completed general education requirements and intro CS courses before transferring."
    }
]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), education=education)

