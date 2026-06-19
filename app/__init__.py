import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

experiences = [
    {
        "title": "Software Engineering Intern",
        "company": "Tech Corp",
        "duration": "Jun 2025 - Aug 2025",
        "description": "Worked on the backend team building APIs and microservices. Helped migrate legacy services to a new architecture."
    },
    {
        "title": "Web Developer",
        "company": "Startup Inc",
        "duration": "Jan 2025 - May 2025",
        "description": "Built and maintained the company website and internal tools. Worked with React and Node.js on a small team."
    },
    {
        "title": "Teaching Assistant",
        "company": "University CS Department",
        "duration": "Sep 2024 - Dec 2024",
        "description": "Helped students with assignments and held office hours for the intro to programming course."
    }
]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), experiences=experiences)

