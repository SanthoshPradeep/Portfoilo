# Portfolio Website

A modern, responsive portfolio website for **Santhosh Pradeep G S**, built with Python Flask backend and modern frontend technologies.

## Features

- 🏠 **Introduction Page** - Welcome page with profile photo and quick overview
- 👤 **About Me** - Detailed information about background, interests, and goals
- 💼 **Projects** - Showcase of projects with technologies and links
- 🛠️ **Skills** - Comprehensive list of technical skills and competencies
- 📄 **Resume** - Professional resume with print and download options
- 📧 **Contact** - Contact form with API endpoint for message submissions

## Student Information

- **Name:** Santhosh Pradeep G S
- **Academic Period:** 2023-2027
- **College:** Annapoorana Engineering College

## Technology Stack

### Backend
- Python 3.x
- Flask (Web Framework)

### Frontend
- HTML5
- CSS3 (Modern responsive design)
- JavaScript (Vanilla JS)
- Font Awesome (Icons)

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd port
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Add your profile photo**
   - Place your profile photo in `static/images/` directory
   - Name it `profile.jpg` (or update the path in `templates/index.html`)

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access the website**
   - Open your browser and go to: `http://localhost:5000`

## Project Structure

```
port/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Introduction page
│   ├── about.html        # About me page
│   ├── projects.html     # Projects page
│   ├── skills.html       # Skills page
│   ├── resume.html       # Resume page
│   └── contact.html      # Contact page
└── static/               # Static files
    ├── css/
    │   └── style.css     # Main stylesheet
    ├── js/
    │   └── script.js     # JavaScript functionality
    └── images/           # Images directory (add profile.jpg here)
```

## Customization

### Update Personal Information

Edit the `STUDENT_INFO` dictionary in `app.py`:

```python
STUDENT_INFO = {
    'name': 'Your Name',
    'academic_period': '2023-2027',
    'college': 'Your College Name',
    'email': 'your.email@example.com',
    'phone': '+91 XXXXX XXXXX',
    'location': 'Your Location'
}
```

### Add Projects

Edit the `PROJECTS` list in `app.py` to add or modify projects:

```python
PROJECTS = [
    {
        'id': 1,
        'title': 'Project Name',
        'description': 'Project description',
        'technologies': ['Tech1', 'Tech2'],
        'github': 'https://github.com/username/repo',
        'live': 'https://live-demo-url.com'
    },
    # Add more projects...
]
```

### Update Skills

Modify the `SKILLS` dictionary in `app.py`:

```python
SKILLS = {
    'programming_languages': ['Python', 'Java', ...],
    'web_technologies': ['HTML5', 'CSS3', ...],
    # Add more categories...
}
```

### Update Social Media Links

Edit the social media links in:
- `templates/base.html` (footer)
- `templates/contact.html` (contact section)

## API Endpoints

- `GET /` - Introduction page
- `GET /about` - About me page
- `GET /projects` - Projects page
- `GET /skills` - Skills page
- `GET /resume` - Resume page
- `GET /contact` - Contact page
- `POST /api/contact` - Contact form submission API

## Features Overview

### Responsive Design
- Mobile-friendly navigation with hamburger menu
- Responsive grid layouts
- Optimized for all screen sizes

### Modern UI/UX
- Smooth animations and transitions
- Gradient backgrounds
- Card-based layouts
- Professional color scheme

### Contact Form
- Form validation
- API endpoint for submissions
- Success/error messaging

## Future Enhancements

- Email integration for contact form
- Database integration for projects
- Blog section
- Dark mode toggle
- PDF resume generation
- Analytics integration

## License

This project is open source and available for personal use.

## Contact

For any questions or suggestions, feel free to reach out!

---

**Built with ❤️ by Santhosh Pradeep G S**

