# Django Modular Quiz App

A modular quiz application built with Django, designed for easy maintenance and scalability.  
This project splits features into separate Django apps like accounts, dashboard, and quiz for a clean architecture.

## Features

- Modular app structure for better code organization
- User authentication (accounts module)
- Quiz management and taking quizzes (quiz module)
- Dashboard for user progress and statistics
- Easy to extend and maintain

## Tech Stack

- Python 3.x
- Django 5.2.x
- Bootstrap 5 (for frontend styling)

## Getting Started

### Prerequisites

- Python 3.8+ installed
- pip (Python package manager)

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/zalwan/django-modular-quiz-app.git
   cd django-modular-quiz-app
   ```

2. Create a virtual environment (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations

   ```bash
   python manage.py migrate
   ```

5. Run the development server

   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit `http://localhost:8000`

## Usage

- Register a new user or login
- Create and take quizzes
- View your progress on the dashboard

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is open source and available under the MIT License.

---

[GitHub](https://github.com/zalwan)
