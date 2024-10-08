from kivy.config import Config

# Menambahkan SDL2 sebagai input provider
Config.set('input', 'mouse', 'mouse,disable_multitouch')

# Nonaktifkan virtual keyboard
Config.set('kivy', 'keyboard_mode', 'system')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login_screen import LoginScreen
from main_screen import MainScreen
from absensi_screen import AbsensiScreen

class GajiKaryawanApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AbsensiScreen(name='absensi'))
        return sm

if __name__ == '__main__':
    GajiKaryawanApp().run()
