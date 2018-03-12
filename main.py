import os

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

from libs.navigationdrawer import NavigationDrawer
from kivymd.theming import ThemeManager
from config import KV_DIR


class StartScreen(BoxLayout):
    pass


class AboutScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        self.add_widget(SettingsScreen(name="settings"))
        self.add_widget(AboutScreen(name="about"))


class Navigator(NavigationDrawer):
    title = StringProperty('Navigation')


class NavigateApp(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        self.load_all_kv_files(KV_DIR)
        main_widget = Builder.load_file(os.path.join(KV_DIR, "startscreen.kv"))
        self.nav_drawer = Navigator()
        return main_widget

    def load_all_kv_files(self, directory_kv_files):
        for kv_file in os.listdir(directory_kv_files):
            kv_file = os.path.join(directory_kv_files, kv_file)
            if os.path.isfile(kv_file):
                with open(kv_file) as kv:
                    Builder.load_string(kv.read())

    def show_about(self, *args):
        self.root.ids.manager.current = "about"
        return True

    def show_settings(self, *args):
        self.root.ids.manager.current = "settings"
        return True

NavigateApp().run()
