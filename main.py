from kivy.app import App
from kivy.uix.label import Label

class AviatorPredictor(App):
    def build(self):
        return Label(text='Hola Aviator 🔥', font_size='40sp')

if __name__ == '__main__':
    AviatorPredictor().run()
