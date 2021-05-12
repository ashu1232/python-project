import pyaudio
import pyttsx3
import wikipedia
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
      engine.say(audio)
      engine.runAndWait()

def wishMe():
      speak("i am your assistant:")
      
def takeCommand():
      r=sr.Recognizer()

      with sr.Microphone() as source:
             print('listening...')
             r.pause_threshold=1
             r.energy_threshold=2000
             audio=r.listen(source)
             
      try:
            query = r.recognize_google(audio,language='en-in')
            print("Recognizing....")
            print(f"User said: {query}\n")
      except Exception as e:
            

            print("Say That again please...")

if __name__ == "__main__":
      wishMe()
      while True:
            query=takeCommand()

            if 'wikipedia' in query:
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
