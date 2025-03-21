import os
import re

# Complete course structure data from all screenshots
course_sections = [
    # Beginner section
    "Day 1 - Beginner - Working with Variables in Python to Manage Data",
    "Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings",
    "Day 3 - Beginner - Control Flow and Logical Operators",
    "Day 4 - Beginner - Randomisation and Python Lists",
    "Day 5 - Beginner - Python Loops",
    "Day 6 - Beginner - Python Functions & Karel",
    "Day 7 - Beginner - Hangman",
    "Day 8 - Beginner - Function Parameters & Caesar Cipher",
    "Day 9 - Beginner - Dictionaries, Nesting and the Secret Auction",
    "Day 10 - Beginner - Functions with Outputs",
    "Day 11 - Beginner - The Blackjack Capstone Project",
    "Day 12 - Beginner - Scope & Number Guessing Game",
    "Day 13 - Beginner - Debugging: How to Find and Fix Errors in your Code",
    "Day 14 - Beginner - Higher Lower Game Project",
    "Day 15 - Intermediate - Local Development Environment Setup & the Coffee Machine",
    
    # Intermediate section
    "Day 16 - Intermediate - Object Oriented Programming (OOP)",
    "Day 17 - Intermediate - The Quiz Project & the Benefits of OOP",
    "Day 18 - Intermediate - Turtle & the Graphical User Interface (GUI)",
    "Day 19 - Intermediate - Instances, State and Higher Order Functions",
    "Day 20 - Intermediate - Build the Snake Game Part 1: Animation & Coordinates",
    "Day 21 - Intermediate - Build the Snake Game Part 2: Inheritance & List Slicing",
    "Day 22 - Intermediate - Build Pong: The Famous Arcade Game",
    "Day 23 - Intermediate - The Turtle Crossing Capstone Project",
    "Day 24 - Intermediate - Files, Directories and Paths",
    "Day 25 - Intermediate - Working with CSV Data and the Pandas Library",
    "Day 26 - Intermediate - List Comprehension and the NATO Alphabet",
    "Day 27 - Intermediate - Tkinter, *args, **kwargs and Creating GUI Programs",
    "Day 28 - Intermediate - Tkinter, Dynamic Typing and the Pomodoro GUI Application",
    "Day 29 - Intermediate - Building a Password Manager GUI App with Tkinter",
    "Day 30 - Intermediate - Errors, Exceptions and JSON Data: Improving the Password",
    "Day 31 - Intermediate - Flash Card App Capstone Project",
    
    # Intermediate+ section
    "Day 32 - Intermediate+ Send Email (smtplib) & Manage Dates (datetime)",
    "Day 33 - Intermediate+ API Endpoints & API Parameters - ISS Overhead Notifier",
    "Day 34 - Intermediate+ API Practice - Creating a GUI Quiz App",
    "Day 35 - Intermediate+ Keys, Authentication & Environment Variables: Send SMS",
    "Day 36 - Intermediate+ Stock Trading News Alert Project",
    "Day 37 - Intermediate+ Habit Tracking Project: API Post Requests & Headers",
    "Day 38 - Intermediate+ Workout Tracking Using Google Sheets",
    "Day 39 - Intermediate+ Capstone Part 1: Flight Deal Finder",
    "Day 40 - Intermediate+ Capstone Part 2: Flight Club",
    
    # Web Foundation section
    "Day 41 - Web Foundation - Introduction to HTML",
    "Day 42 - Web Foundation - Intermediate HTML",
    "Day 43 - Web Foundation - Introduction to CSS",
    "Day 44 - Web Foundation - Intermediate CSS",
    
    # Intermediate+ Web Scraping and Development
    "Day 45 - Intermediate+ Web Scraping with Beautiful Soup",
    "Day 46 - Intermediate+ Create a Spotify Playlist using the Musical Time Machine",
    "Day 47 - Intermediate+ Create an Automated Amazon Price Tracker",
    "Day 48 - Intermediate+ Selenium Webdriver Browser and Game Playing Bot",
    "Day 49 - Intermediate+ Automating Job Applications on LinkedIn",
    "Day 50 - Intermediate+ Auto Tinder Swiping Bot",
    "Day 51 - Intermediate+ Internet Speed Twitter Complaint Bot",
    "Day 52 - Intermediate+ Instagram Follower Bot",
    "Day 53 - Intermediate+ Web Scraping Capstone - Data Entry Job Automation",
    "Day 54 - Intermediate+ Introduction to Web Development with Flask",
    "Day 55 - Intermediate+ HTML & URL Parsing in Flask and the Higher Lower Game",
    "Day 56 - Intermediate+ Rendering HTML/Static files and Using Website Templates",
    "Day 57 - Intermediate+ Templating with Jinja in Flask Applications",
    "Day 58 - Web Foundation Bootstrap",
    
    # Advanced web development section
    "Day 59 - Advanced - Blog Capstone Project Part 2 - Adding Styling",
    "Day 60 - Advanced - Make POST Requests with Flask and HTML Forms",
    "Day 61 - Advanced - Building Advanced Forms with Flask-WTForms",
    "Day 62 - Advanced - Flask, WTForms, Bootstrap and CSV - Coffee & Wifi Project",
    "Day 63 - Advanced - Databases with SQLite and SQLAlchemy",
    "Day 64 - Advanced - My Top 10 Movies Website",
    "Day 65 - Web Design School - How to Create a Website that People will Love",
    "Day 66 - Advanced - Building Your Own API with RESTful Routing",
    "Day 67 - Advanced - Blog Capstone Project Part 3 - RESTful Routing",
    "Day 68 - Advanced - Authentication with Flask",
    "Day 69 - Advanced - Blog Capstone Project Part 4 - Adding Users",
    "Day 70 - Advanced - Git, GitHub and Version Control",
    "Day 71 - Advanced - Deploying Your Web Application",
    "Day 72 - Advanced - Data Exploration with Pandas: College Major v.s. Your Salary",
    
    # Advanced data section
    "Day 73 - Advanced - Data Visualisation with Matplotlib: Programming Languages",
    "Day 74 - Advanced - Aggregate & Merge Data with Pandas: Analyse the LEGO Dataset",
    "Day 75 - Advanced - Google Trends Data: Resampling and Visualising Time Series",
    "Day 76 - Advanced - Beautiful Plotly Charts & Analysing the Android App Store",
    "Day 77 - Advanced - Computation with NumPy and N-Dimensional Arrays",
    "Day 78 - Advanced - Linear Regression and Data Visualisation with Seaborn",
    "Day 79 - Advanced - Analysing the Nobel Prize with Plotly, Matplotlib & Seaborn",
    "Day 80 - Advanced - The Tragic Discovery of Handwashing: t-Tests & Distributions",
    "Day 81 - Advanced - Capstone Project - Predict House Prices",
    
    # Professional Portfolio Projects
    "Day 82 - Professional Portfolio Project - [Python Scripting]",
    "Day 83 - Professional Portfolio Project - [Python Web Development]",
    "Day 84 - Professional Portfolio Project - [Python Scripting]",
    "Day 85 - Professional Portfolio Project - [GUI]",
    "Day 86 - Professional Portfolio Project - [GUI]",
    "Day 87 - Professional Portfolio Project - [Game]",
    "Day 88 - Professional Portfolio Project - [Web Development]",
    "Day 89 - Professional Portfolio Project - [Web Development]",
    "Day 90 - Professional Portfolio Project - [GUI Desktop App]",
    "Day 91 - Professional Portfolio Project - [HTTP Requests & APIs]",
    "Day 92 - Professional Portfolio Project - [Image Processing & Data Science]",
    "Day 93 - Professional Portfolio Project - [Web Scraping]",
    "Day 94 - Professional Portfolio Project - [GUI Automation]",
    "Day 95 - Professional Portfolio Project - [Game]",
    "Day 96 - Professional Portfolio Project - [HTTP Requests & APIs]",
    "Day 97 - Professional Portfolio Project - [Web Development]",
    "Day 98 - Professional Portfolio Project - [Python Automation]",
    "Day 99 - Professional Portfolio Project - [Data Science]",
    "Day 100 - Professional Portfolio Project - [Data Science]",
    
    # Bonus
    "Final Stretch"
]

def clean_folder_name(title):
    # Extract day number
    day_match = re.search(r'Day (\d+)', title)
    day_num = day_match.group(1) if day_match else "00"
    day_num = day_num.zfill(2)  # Ensure two digits
    
    # Extract level
    level_match = re.search(r'- (Beginner|Intermediate\+?|Advanced|Web Foundation|Web Design School|Professional Portfolio Project) -?', title)
    level = level_match.group(1) if level_match else "Other"
    
    # Handle special case for Final Stretch
    if title == "Final Stretch":
        return "day-101-final-stretch"
    
    # Shorten level names
    level_short = level.lower()
    if level_short == "intermediate+":
        level_short = "int-plus"
    elif level_short == "intermediate":
        level_short = "int"
    elif level_short == "beginner":
        level_short = "beg"
    elif level_short == "advanced":
        level_short = "adv"
    elif level_short == "web foundation":
        level_short = "web"
    elif level_short == "web design school":
        level_short = "web-design"
    elif level_short == "professional portfolio project":
        level_short = "prof"
    
    # Extract main topic
    topic_match = re.search(r'- [^-]+ -\s?(.+)', title)
    topic = topic_match.group(1) if topic_match else ""
    
    # For professional portfolio projects, extract the category
    if level == "Professional Portfolio Project":
        category_match = re.search(r'\[(.*?)\]', title)
        if category_match:
            topic = category_match.group(1)
    
    # Shorten and clean topic
    if topic:
        topic_words = topic.split()
        if len(topic_words) > 4:
            short_topic = " ".join(topic_words[:4])
        else:
            short_topic = topic
            
        # Clean the topic for a filename
        short_topic = short_topic.replace('&', 'and')
        short_topic = re.sub(r'[^\w\s-]', '', short_topic)  # Remove special characters
        short_topic = short_topic.replace(' ', '-').lower()  # Replace spaces with hyphens
        
        return f"day-{day_num}-{level_short}-{short_topic}"
    else:
        return f"day-{day_num}-{level_short}"

def create_directory_structure(base_path="python-100-days-of-code"):
    # Create base directory
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"Created base directory: {base_path}")
    
    # Create .gitignore file
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS specific
.DS_Store
Thumbs.db
"""
    
    with open(os.path.join(base_path, ".gitignore"), "w") as f:
        f.write(gitignore_content)
    
    # Create README.md
    readme_content = """# 100 Days of Code: The Complete Python Pro Bootcamp

This repository contains my code and projects from the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp".

## Course Structure

The course is divided into sections:
- Beginner (Days 1-14)
- Intermediate (Days 15-31)
- Intermediate+ (Days 32-57)
- Web Development with Flask (Days 54-58)
- Advanced Web Development (Days 59-71)
- Advanced Data Analysis (Days 72-80)
- Professional Portfolio Projects (Days 81-100)

## Projects

Each day includes different coding exercises and projects to build Python skills, from beginner concepts to advanced applications.

## Repository Organization

The repository is organized by day, with each folder following the naming convention:
```
day-XX-level-project-name
```

For example:
- day-01-beg-working-with-variables
- day-34-int-plus-api-practice
- day-76-adv-beautiful-plotly-charts
"""
    
    with open(os.path.join(base_path, "README.md"), "w") as f:
        f.write(readme_content)
    
    # Create folder for each day
    for section in course_sections:
        folder_name = clean_folder_name(section)
        folder_path = os.path.join(base_path, folder_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
            # Create a basic README for each day
            day_match = re.search(r'Day (\d+)', section)
            day_num = day_match.group(1) if day_match else "Unknown"
            
            # Skip the "Final Stretch" special case
            if section == "Final Stretch":
                day_readme = """# Final Stretch

## Overview
Additional resources and final notes from the "100 Days of Code" Python course.

## Contents
- [Key resources and references]
- [Course completion materials]
"""
            else:
                # Extract the main title (removing "Day XX - Level - " prefix)
                title_match = re.search(r'Day \d+ - [^-]+ - (.+)', section)
                title = title_match.group(1) if title_match else section
                
                day_readme = f"""# Day {day_num}: {title}

## Overview
Code and exercises from Day {day_num} of the "100 Days of Code" Python course.

## Projects
- [Main Project Description]

## Concepts
- [Key concepts covered]
"""
            
            with open(os.path.join(folder_path, "README.md"), "w") as f:
                f.write(day_readme)
                
            # Create an empty main.py file (except for Final Stretch)
            if section != "Final Stretch":
                with open(os.path.join(folder_path, "main.py"), "w") as f:
                    f.write(f"""# Day {day_num} - {section.split(' - ', 2)[-1] if ' - ' in section else section}
# 100 Days of Code - Python Pro Bootcamp

# Your code here
""")
                
        print(f"Created: {folder_name}")

if __name__ == "__main__":
    create_directory_structure()
    print("\nDirectory structure created successfully!")
    print("\nTo initialize this as a git repository:")
    print("1. cd python-100-days-of-code")
    print("2. git init")
    print("3. git add .")
    print("4. git commit -m 'Initial setup of 100 Days of Code course'")
    print("5. git branch -M main")
    print("6. git remote add origin https://github.com/YOUR-USERNAME/python-100-days-of-code.git")
    print("7. git push -u origin main")
