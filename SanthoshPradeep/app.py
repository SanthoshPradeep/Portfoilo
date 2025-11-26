from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'

# Student information
STUDENT_INFO = {
    'name': 'Santhosh Pradeep G S',
    'academic_period': '2023-2027',
    'college': 'Annapoorana Engineering College, Salem, Tamilnadu-636 106',
    'email': 'santhoshpradeep2809@gmail.com',
    'phone': '+91 93459 29313',
    'location': 'India'
}

# Sample projects data
PROJECTS = [
    {
        'id': 1,
        'title': 'Project 1',
        'description': 'Description of your first project. Add details about technologies used and what you learned.',
        'technologies': ['Python', 'Flask', 'HTML/CSS'],
        'github': 'https://github.com/yourusername/project1',
        'live': '#'
    },
    {
        'id': 2,
        'title': 'Project 2',
        'description': 'Description of your second project. Showcase your skills and achievements.',
        'technologies': ['JavaScript', 'React', 'Node.js'],
        'github': 'https://github.com/yourusername/project2',
        'live': '#'
    },
    {
        'id': 3,
        'title': 'Project 3',
        'description': 'Description of your third project. Highlight your problem-solving abilities.',
        'technologies': ['Python', 'Django', 'PostgreSQL'],
        'github': 'https://github.com/yourusername/project3',
        'live': '#'
    }
]

# Skills data
SKILLS = {
    'programming_languages': ['Python', 'Java', 'C++', 'JavaScript'],
    'web_technologies': ['HTML5', 'CSS3', 'JavaScript', 'React', 'Flask', 'Django'],
    'databases': ['MySQL', 'PostgreSQL', 'MongoDB'],
    'tools': ['Git', 'GitHub', 'VS Code', 'Postman'],
    'other': ['Data Structures', 'Algorithms', 'Object-Oriented Programming']
}

@app.route('/')
def index():
    """Home/Introduction page"""
    return render_template('index.html', student=STUDENT_INFO)

@app.route('/about')
def about():
    """About me page"""
    return render_template('about.html', student=STUDENT_INFO)

@app.route('/projects')
def projects():
    """Projects page"""
    return render_template('projects.html', student=STUDENT_INFO, projects=PROJECTS)

@app.route('/skills')
def skills():
    """Skills page"""
    return render_template('skills.html', student=STUDENT_INFO, skills=SKILLS)

@app.route('/resume')
def resume():
    """Resume page"""
    return render_template('resume.html', student=STUDENT_INFO, skills=SKILLS, projects=PROJECTS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page"""
    if request.method == 'POST':
        data = request.get_json()
        # Here you can add email sending functionality
        # For now, we'll just return a success message
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.'
        })
    return render_template('contact.html', student=STUDENT_INFO)

@app.route('/api/contact', methods=['POST'])
def contact_api():
    """API endpoint for contact form"""
    try:
        data = request.get_json()
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        # Validate required fields
        if not name or not email or not message:
            return jsonify({
                'success': False,
                'message': 'Please fill in all required fields.'
            }), 400
        
        # Here you can add logic to save to database or send email
        # For now, we'll just log it
        print(f"Contact form submission from {name} ({email}): {message}")
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        }), 500

if __name__ == '__main__':
    # Create uploads directory if it doesn't exist
    os.makedirs('static/images', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)


