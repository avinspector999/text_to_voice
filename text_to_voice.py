from pathlib import Path
from gtts import gTTS
import os

def text_to_speech(text, language='en', filename='output.mp3'):
    """Converts the given text to speech and saves it as an MP3 file.

    Args:
        text (str): The text to convert.
        language (str, optional): The language of the text (default is 'en' for English).
        filename (str, optional): The name of the output MP3 file (default is 'output.mp3').
    """
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    # Play the generated audio (optional, may require additional libraries or setup)
    # os.system("mpg321 " + filename)  # For Linux
    # os.system("afplay " + filename)   # For macOS
    # os.system("start " + filename)    # For Windows

if __name__ == "__main__":
    text = "Hello, this is a test of the text to speech function."
    text_to_speech(text)
    print("Text converted to speech and saved as output.mp3")

text_to_speech(text="Hi, I am dancer also and a fighter also"
              ,language='en'
              ,filename="\\Users\\Rajasri\\Downloads\\output.mp3")

text_to_speech(text="hi, my name is maha"
              ,language='en'
              ,filename="\\Users\\Rajasri\\Downloads\\Maha_output.mp3")
