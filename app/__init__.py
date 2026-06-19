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
        "description": "Worked on the backend team building APIs and microservices."
    },
    {
        "title": "Web Developer",
        "company": "Startup Inc",
        "duration": "Jan 2025 - May 2025",
        "description": "Built and maintained the company website and internal tools."
    },
    {
        "title": "Teaching Assistant",
        "company": "University CS Department",
        "duration": "Sep 2024 - Dec 2024",
        "description": "Helped students with assignments and held office hours."
    }
]

education = [
    {
        "school": "University of Placeholder",
        "degree": "B.S. Computer Science",
        "duration": "2022 - 2026"
    },
    {
        "school": "Community College",
        "degree": "Associate's in General Studies",
        "duration": "2020 - 2022"
    }
]

hobbies = [
    {"name": "Hiking", "description": "Love exploring trails and getting summit views."},
    {"name": "Gaming", "description": "Currently grinding ranked in Valorant."},
    {"name": "Cooking", "description": "My specialty is stir fry but getting into baking."}
]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"),
                           experiences=experiences, education=education, hobbies=hobbies)

