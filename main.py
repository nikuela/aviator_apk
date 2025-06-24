import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.graphics.texture import Texture
from PIL import Image as PILImage
import pytesseract
import io

kivy.require('2.0.0')

class OCRBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(OCRBoxLayout, self).__init__(orientation='vertical', **kwargs)

        self.choose = FileChooserIconView(filters=['*.png', '*.jpg', '*.jpeg'], size_hint=(1, 0.6))
        self.choose.bind(on_selection=self.selected)
        self.add_widget(self.choose)

        self.image = Image(size_hint=(1, 0.4))
        self.add_widget(self.image)

        self.result_label = Label(text='Texto detectado aparecerá aquí', size_hint=(1, 0.2))
        self.add_widget(self.result_label)

    def selected(self, *args):
        try:
            path = self.choose.selection[0]
            img = PILImage.open(path)
            self.display_image(img)

            text = pytesseract.image_to_string(img, config='--psm 6')
            self.result_label.text = f'Texto detectado:\n{text}'
        except Exception as e:
            self.result_label.text = f'Error al procesar la imagen: {str(e)}'

    def display_image(self, pil_img):
        pil_img = pil_img.convert('RGB')
        w, h = pil_img.size
        texture = Texture.create(size=(w, h))
        texture.blit_buffer(pil_img.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
        texture.flip_vertical()
        self.image.texture = texture

class AviatorPredictorApp(App):
    def build(self):
        return OCRBoxLayout()

if __name__ == '__main__':
    AviatorPredictorApp().run()
