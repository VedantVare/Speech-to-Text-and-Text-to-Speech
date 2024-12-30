# Speech Assistant

This is a simple Python program that provides two main functionalities:
1. **Speech to Text**: Converts your spoken words into text.
2. **Text to Speech**: Converts typed text into spoken words.

## Features
- Recognizes speech using a microphone.
- Converts text to speech using a built-in voice.
- Easy-to-use menu for selecting functionality.

## Requirements
- Python 3.7 or higher
- `pyttsx3` library for text-to-speech functionality.
- `speech_recognition` library for speech-to-text functionality.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/speech-assistant.git
   cd speech-assistant
   ```
2. Install the required libraries:
   ```bash
   pip install pyttsx3 SpeechRecognition
   ```

## Usage
1. Run the script:
   ```bash
   python speech_assistant.py
   ```
2. Choose an option:
   - Press `1` for **Speech to Text**:
     - Speak into the microphone.
     - The program will print the recognized text on the screen.
     - Say "Exit" or "End" to terminate.
   - Press `2` for **Text to Speech**:
     - Enter a sentence.
     - The program will read it out loud.
     - Type "Exit" or "End" to terminate.

## Notes
- Make sure your microphone is working for the Speech-to-Text functionality.
- You can adjust the speaking rate and voice settings in the script.

## License
Feel free to use and modify this project as you wish. Attribution is appreciated but not required.
