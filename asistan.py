from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser


r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
        return voice

#komutlar
def response(voice):
#karşılama komutları
    if "merhaba" in voice:
        speak("sanada merhaba")

    if "selam" in voice:
        speak("aleyküm selam")

    if "günaydın" in voice:
        speak("sanada günaydın")

    if "iyi akşamlar" in voice:
        speak("sanada iyi akşamlar")
    
    if "selamın aleyküm" in voice:
        speak("aleyküm selam")
    
    if "nasılsın" in voice:
        speak("iyiyim sen nasılsın")
    
    if "bay bay" in voice:
        speak("bay bay")
        exit()

    if "ne yapıyorsun" in voice:
        karar = ["makale araştırıyorum","iyiyim sen ne yapıyorsun","kendimi geliştiriyorum","dil çalışıyorum","hayata nasıl geldiğimi sorguluyorum","sanane",]
        karar = random.choice(karar)
        speak(karar)
#Müzikleri aç
    if "müzik aç" in voice:
        path = 'C:\\Users\\RFB\\Music'
        os.startfile(path)
        speak("Hemen Açıyorum")
#indirilenleri aç
    if "i̇ndirilenleri aç" in voice:
        path = 'C:\\Users\\RFB\\Downloads'
        os.startfile(path)
        speak("Hemen Açıyorum")
#saat
    if "saat kaç" in voice:
        secim = ["hemen bakıyorum:","saat:","bakıp geliyorum",]
        saat = datetime.now().strftime("%H:%M")
        secim = random.choice(secim)
        speak(secim + saat)
#günlerden ne
    if "günlerden ne" in voice:
        gun = time.strftime("%A")
        if gun == "Monday":
            gun = "pazartesi"

        if gun == "Tuesday":
            gun = "salı"
        
        if gun == "Wednesday":
            gun = "çarşamba"
        
        if gun == "Tuesday":
            gun = "perşembe"
        
        if gun == "Friday":
            gun = "cuma"
        
        if gun == "Sturday":
            gun = "Cumartesi"

        if gun == "Sunday":
            gun = "pazar"
        speak(gun)
#google arama
    if "google'da ara" in voice:
        speak("ne aramamı istersin")
        ara = record()
        url = "https://www.google.com.tr/search?q={}". format(ara)
        webbrowser.get().open(url)
        speak("{} sonuçları listeliyorum". format(ara))

###############################################
def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)



speak("efendim")

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice)
        response(voice)




