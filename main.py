from kivy.app import App
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.colorpicker import ColorPicker
from kivymd.uix.button import MDIconButton

from kivymd.icon_definitions import md_icons
from kivymd.uix.label import MDIcon

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRectangleFlatButton
import threading

import scripts.calculateFunctions as calculateFunctions

Builder.load_file('main.kv')
Window.size = (700, 420)

class MainScreen(MDScreen):
    pass

class Myapp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"

        sm = MDScreenManager(size_hint=(1, 1))
        sm.add_widget(MainScreen(name="mainScreen"))
        return sm

if __name__ == "__main__":
    Myapp().run()