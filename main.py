import os

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

# from kivymd.navigationdrawer import NavigationDrawer
from libs.navigationdrawer import NavigationDrawer
from vendor.kivymd.theming import ThemeManager
from config import KV_DIR

class StartScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


class Navigator(NavigationDrawer):
    image_source = StringProperty('data/images/me.jpg')
    title = StringProperty('Navigation')


class NavigateApp(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        self.load_all_kv_files(KV_DIR)
        self.screen = ScreenManager()
        self.screen_start = StartScreen(name='start')
        self.screen_about = AboutScreen(name='about')
        self.screen_setting = SettingsScreen(name='settings')
        self.screen.add_widget( self.screen_start)
        self.screen.add_widget(self.screen_about)
        self.screen.add_widget(self.screen_setting)
        self.screen.current = "start"
        # main_widget = Builder.load_file(os.path.join(KV_DIR, "main.kv"))
        self.nav_drawer = Navigator()
        return self.screen

    def load_all_kv_files(self, directory_kv_files):
        for kv_file in os.listdir(directory_kv_files):
            kv_file = os.path.join(directory_kv_files, kv_file)
            if os.path.isfile(kv_file):
                with open(kv_file, encoding='utf-8') as kv:
                    Builder.load_string(kv.read())

    def show_about(self, *args):
        self.screen.current = "about"
        return True

NavigateApp().run()
