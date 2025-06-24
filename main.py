import kivy
from kivy.app import App
from kivy.uix.label import Label

class AviatorPredictorApp(App):
    def build(self):
        return Label(text='Aviator Predictor funcionando...')

if __name__ == '__main__':
    AviatorPredictorApp().run()
