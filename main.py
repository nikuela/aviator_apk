from kivy.app import App
from kivy.uix.label import Label

class MiApp(App):
    def build(self):
        return Label(text="¡Mi APK se generó con éxito!", font_size=24)

if __name__ == "__main__":
    MiApp().run()
