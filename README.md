# Voice-Controlled Application with Wake Word Detection

## Introduction

This project is a voice-controlled application that utilizes wake word detection to trigger voice commands. It is designed to run on multiple platforms, including Windows, macOS, and Linux. The wake word "hello simeranya" is used to activate the voice recognition system.

## Requirements

- Python 3.7+
- Django (for web interface)
- pvporcupine
- pvrecorder
- speech_recognition
- Other dependencies as specified in your `requirements.txt` or `Pipfile`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/voice-controlled-app.git
   cd voice-controlled-app

Install the required packages using pip or pipenv:
```bash
    pip install -r requirements.txt
    # or using pipenv
    pipenv install
```



## Usage
1. Run the Django development server:

````
python manage.py runserver
````

2. Open a web browser and navigate to http://localhost:8000/ to access the application.


3. The application listens for the wake word "hello simeranya." When detected, you can give voice commands, and the application will process them using Google Speech Recognition.


```
You can save this content in a file with the ".md" extension (e.g., "README.md") to create a Markdown README file for your project.
```