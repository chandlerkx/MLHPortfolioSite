import os
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

experiences = [
    {
        "title": "Software Engineering Intern",
        "company": "TD",
        "duration": "May 2026 - Aug 2026",
        "description": "QE Dev Tooling"
    },
    {
        "title": "Software Engineering Intern",
        "company": "BMO",
        "duration": "Sep 2025 - April 2026",
        "description": "Cloud Development"
    },
    {
        "title": "Software Engineering Intern",
        "company": "Roche",
        "duration": "Jan 2025 - Aug 2025",
        "description": "First intern hire in PDIE!"
    }
]

education = [
    {
        "school": "University of Western Ontario",
        "degree": "B.S. Computer Science",
        "duration": "2022 - 2027"
    }
]

hobbies = [
    {"name": "Skateboarding", "description": "Cruising the streets and trying new tricks at the local park."},
    {"name": "Volleyball", "description": "Playing setter for my intramural team. Always down for a beach game."},
    {"name": "Gaming", "description": "Currently grinding ranked in Valorant. I play a mix of FPS and RPGs."}
]

locations = [
    {"lat": 39.3999, "lng": -8.2245, "name": "Portugal"},
    {"lat": 49.2827, "lng": -123.1207, "name": "Vancouver"},
    {"lat": 53.9333, "lng": -116.5765, "name": "Alberta"},
    {"lat": 49.8951, "lng": -97.1384, "name": "Winnipeg"},
    {"lat": 27.9944, "lng": -81.7603, "name": "Florida"},
    {"lat": 35.8617, "lng": 104.1954, "name": "China"},
    {"lat": 22.3193, "lng": 114.1694, "name": "Hong Kong"},
    {"lat": 23.1291, "lng": 113.2644, "name": "Guangzhou"},
    {"lat": 22.1987, "lng": 113.5439, "name": "Macau"},
    {"lat": 18.7357, "lng": -70.1627, "name": "Dominican Republic"},
    {"lat": 25.0343, "lng": -77.3963, "name": "Bahamas"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/portfolio')
def portfolio_data():
    return jsonify({
        "experiences": experiences,
        "education": education,
        "hobbies": hobbies,
        "locations": locations
    })

# Fallback route for React Router (if using client-side routing)
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')
