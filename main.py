
from kivy.app import App
from kivy.uix.label import Label

class AviatorApp(App):
    def build(self):
        return Label(text='Aviator Predictor')

if __name__ == '__main__':
    AviatorApp().run()
