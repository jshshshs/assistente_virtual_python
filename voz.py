import pyttsx3

class voz():

    def _init_(self):
        pass

    def fala(self, texto):
        engine = pyttsx3.init('sapi5')
        engine.say(texto)
        engine.runAndWait()
