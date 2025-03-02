import speech_recognition as sr
import pyttsx3  

def text_to_speech(text, voice_id=None):
    """Converts text to speech using pyttsx3."""
    engine = pyttsx3.init()

    if voice_id:
        engine.setProperty("voice", voice_id)  # Set a specific voice if needed
    
    engine.say(text)
    engine.runAndWait()

def speech_to_text(language="hi-IN"):
    """Captures audio from the microphone and converts it to text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        print("\n🎤 Listening... Please speak.")
        recognizer.adjust_for_ambient_noise(mic)  # Reduces background noise
        audio_data = recognizer.listen(mic)

    try:
        # Convert audio to text using Google's Speech Recognition API
        transcribed_text = recognizer.recognize_google(audio_data, language=language)
        print("✅ Recognized Speech:", transcribed_text)
        return transcribed_text

    except sr.UnknownValueError:
        print("⚠️ Sorry, I couldn't understand your speech.")
        return ""

    except sr.RequestError as err:
        print(f"🚨 API request failed: {err}")
        return ""

# Example usage
if __name__ == "__main__":
    sample_text = "Hello! How can I assist you today?"
    text_to_speech(sample_text)

    user_response = speech_to_text()
    print("🗣 User said:", user_response)
