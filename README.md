# Speech to Indian Sign Language (ISL) Converter

## Description
This project is a **Speech-to-Indian Sign Language (ISL) Converter** that converts spoken language into ISL gestures. It uses **speech recognition** to capture spoken words and maps them to corresponding ISL signs. The system is designed to assist communication between **speech-impaired individuals and the general public**.

## Features
- **Speech-to-text conversion** using speech recognition
- **Indian Sign Language (ISL) gesture mapping**
- **Web-based interface** for accessibility
- **Database storage** for managing recognized words and gestures
- **User-friendly UI** with responsive design

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (3.x recommended)
- Django (as the web framework)
- Required dependencies from `requirements.txt`

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Speech_to_ISL.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Speech_to_ISL-main
   ```
3. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Apply migrations and set up the database:
   ```sh
   python manage.py migrate
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
7. Open the application in your browser:
   ```
   http://127.0.0.1:8000
   ```

## Directory Structure
```
Speech_to_ISL-main/
│-- manage.py                   # Django project management script
│-- db.sqlite3                   # SQLite database file
│-- requirements.txt             # Dependencies list
│-- setup.py                     # Setup script (if needed)
│-- .venv/                        # Virtual environment (optional)
│-- app/                         # Main application folder
│   ├── models.py                # Database models
│   ├── views.py                 # Application views
│   ├── templates/               # HTML templates for frontend
│   ├── static/                  # CSS, JavaScript, and images
│-- README.md                    # Project documentation
```

## Usage
1. **Start the web application.**
2. **Speak into the microphone.** The system captures speech and converts it to text.
3. **View the corresponding ISL gestures.** The application displays sign language animations or images.

## Future Improvements
- Add **machine learning models** to enhance ISL gesture recognition.
- Implement **real-time video-based sign language translation**.
- Introduce **support for multiple Indian languages**.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for discussions.

## License
This project is open-source under the [MIT License](LICENSE).

