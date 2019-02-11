from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'width', '720')

class MainApp(App):
    def build(self):
        parent = Widget()
        left_btn = Button(height='50dp', width='360dp')
        right_btn = Button(height='50dp', width=left_btn.width, pos=(360,0))
        parent.add_widget(left_btn)
        parent.add_widget(right_btn)
        return parent

if __name__ == '__main__':
    MainApp().run()
