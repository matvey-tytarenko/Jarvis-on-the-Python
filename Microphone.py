import speech_recognition as sr

rec = sr.Recognizer()
sr.pause_threshold = 0.5

def speak():
    with sr.Microphone() as source:
        print("скажите вашу команду...")
        rec.adjust_for_ambient_noise(source=source, duration=0.5)
        audio = rec.listen(source=source)
        query = rec.recognize_google(audio_data=audio, language='ru-RU').lower()
        print(query)