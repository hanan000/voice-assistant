# Voice-Assistant Application with Wake Word Detection

## Introduction

This project is a voice-assistant application that utilizes wake word detection to trigger voice commands. It is designed to run on multiple platforms, including Windows, macOS, and Linux. The wake word <span style="color:red">hello simeranya</span> is used to activate the voice recognition system. If you face any exceptions, please say "alexa" as the wake word instead.

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
   git https://github.com/hanan000/voice-assistant.git
   cd voice_assiatnt
```

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


3. The application listens for the wake word "hello simeranya." When detected, you can give voice commands, and the application will process them using Google Speech Recognition (only in English).

