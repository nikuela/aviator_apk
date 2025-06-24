from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button

class AviatorPredictorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text='Bienvenido a AviatorPredictor', font_size='20sp')
        self.image = Image(source='example.png')  # Reemplaza con tu lógica real
        self.button = Button(text='Analizar Imagen')
        self.button.bind(on_press=self.analyze)

        layout.add_widget(self.label)
        layout.add_widget(self.image)
        layout.add_widget(self.button)

        return layout

    def analyze(self, instance):
        self.label.text = 'Análisis completo. Resultado: 1.76x'  # Simulación

if __name__ == '__main__':
    AviatorPredictorApp().run()
