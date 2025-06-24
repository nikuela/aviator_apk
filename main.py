
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
from camera_capture import capture_ocr_text
from predictor import predict_result

class AviatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.image = Image()
        self.btn = Button(text='Predecir', size_hint=(1, 0.2))
        self.btn.bind(on_press=self.analyze)
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.btn)

        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)
        return self.layout

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buf = cv2.flip(frame, 0).tobytes()
            img_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.image.texture = img_texture
            self.current_frame = frame

    def analyze(self, instance):
        text = capture_ocr_text(self.current_frame)
        prediction = predict_result(text)
        self.btn.text = f'Predicción: {prediction}'

if __name__ == '__main__':
    AviatorApp().run()
# 🚀 Forzando ejecución de workflow build_apk.yml desde IA
