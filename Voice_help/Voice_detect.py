import speech_recognition
import pyaudio


key = "AIzaSyCuy4bCUp3yzNB1JM-NRGvUSV_w69GP4WE"
sor = speech_recognition.Recognizer()
p = pyaudio.PyAudio()
# credentials = GoogleCredentials.get_application_default()

with speech_recognition.Microphone() as microphone:
    sor.adjust_for_ambient_noise(source=microphone, duration=0.8)
    audio = sor.listen(source=microphone)
    query = sor.recognize_google(audio_data=audio, language='ru-Ru'.lower())
    print(query)
finded_add = ['добавить', 'додати', 'add']
finded_del = ['убрать', 'видалити', 'delete']
for add in finded_add:
    if query in add:
        print('добавляю')
        break
    else:
        print('убрать')    
        break
