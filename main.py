import os

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

# from kivymd.navigationdrawer import NavigationDrawer
from libs.navigationdrawer import NavigationDrawer
from vendor.kivymd.theming import ThemeManager
from config import KV_DIR



class About(Screen):
    pass


class Navigator(NavigationDrawer):
    image_source = StringProperty('data/images/me.jpg')
    title = StringProperty('Navigation')


class NavigateApp(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(About(name='about'))
        # main_widget = Builder.load_file(os.path.join(KV_DIR, "main.kv"))
        self.nav_drawer = Navigator()
        return self.sm

    def show_about(self, *args):
        self.nav_drawer.toggle_nav_drawer()
        self.screen.ids.about.ids.label.text = ""

NavigateApp().run()
