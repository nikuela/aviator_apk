from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class AviatorApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        return Label(
            text="🚀 Aviator Predictor APK Generado con Éxito!",
            font_size='20sp',
            color=(1, 1, 1, 1),
            halign="center",
            valign="middle"
        )

if __name__ == '__main__':
    AviatorApp().run()
