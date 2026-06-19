import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

photos = ["IMG_2488.jpg", "IMG_2493.jpg", "IMG_2402.jpg"]

pages = [
    {"name": "Home", "url": "/"},
    {"name": "Hobbies", "url": "/hobbies"}
]

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
    {"name": "Hiking", "image": "hiking.png", "description": "Love exploring trails and getting summit views."},
    {"name": "Gaming", "image": "gaming.png", "description": "Currently grinding ranked in Valorant."},
    {"name": "Cooking", "image": "cooking.png", "description": "My specialty is stir fry but getting into baking."}
]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), 
                           photos=photos, experiences=experiences, education=education, 
                           hobbies=hobbies, pages=pages)

@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html', title="My Hobbies", hobbies=hobbies, pages=pages)
