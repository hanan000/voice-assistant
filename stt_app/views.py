import platform

import pvporcupine
import speech_recognition as sr
from django.shortcuts import render
from helper.config_helper import ConfigurationHelper
from pvrecorder import PvRecorder

config = ConfigurationHelper()


def create_porcupine():
    """Create and return a Porcupine instance based on the configuration and OS.

    Returns:
        A Porcupine instance.
    """
    os_name = platform.system()
    try:
        print(f"{os_name = }")
        if os_name == "Windows":
            keyword_path = f"{config.project_dir()}/{config.get_conf('WINDOWS_KEYWORD_PATH')}"
        elif os_name == "Darwin":
            keyword_path = f"{config.project_dir()}/{config.get_conf('MAC_KEYWORD_PATH')}"
        elif os_name == "Linux":
            keyword_path = f"{config.project_dir()}/{config.get_conf('LINUX_KEYWORD_PATH')}"
        else:
            print("Unsupported operating system")

        return pvporcupine.create(
            access_key=config.get_conf("ACCESS_KEY"), keyword_paths=[keyword_path]
        )
    except Exception as e:
        print(f"An Error occurred: {e}")
        return pvporcupine.create(
            access_key=config.get_conf("ACCESS_KEY"),
            keywords=[config.get_conf("KEYWORDS")],
        )


def index(request):
    """Handle the index page request.

    Args:
        request: Django HTTP request object.

    Returns:
        Django HTTP response object.
    """
    if request.method == "POST":
        # Initialize the recognizer
        recognizer = sr.Recognizer()
        # Initialize the wake word "hello simeranya"
        porcupine = create_porcupine()
        recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

        try:
            recoder.start()
            while True:
                keyword_index = porcupine.process(recoder.read())
                if keyword_index >= 0:
                    print("Wake word detected...")
                    with sr.Microphone() as source:
                        print("Listening for a command...")
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source)
                    try:
                        text = recognizer.recognize_google(audio)
                        print(text)
                    except sr.UnknownValueError:
                        text = "Could not understand audio"
                    except sr.RequestError as e:
                        text = f"Error with the service: {e}"

                    return render(request, "index.html", {"text": text})

        except KeyboardInterrupt:
            recoder.stop()
        finally:
            porcupine.delete()
            recoder.delete()

        return render(request, "index.html")

    else:
        return render(request, "index.html")
