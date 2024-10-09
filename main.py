from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login_screen import LoginScreen
from main_screen import MainScreen
from profil_screen import ProfilScreen
from absensi_screen import AbsensiScreen
from karyawan_screen import EmployeeRegistrationScreen, EmployeeListScreen

Config.set('input', 'mouse', 'mouse,disable_multitouch')

Config.set('kivy', 'keyboard_mode', 'system')

class GajiKaryawanApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ProfilScreen(name='profil'))
        sm.add_widget(AbsensiScreen(name='absensi'))
        sm.add_widget(EmployeeRegistrationScreen(name='employee_registration'))
        sm.add_widget(EmployeeListScreen(name='employee_list'))
        return sm

if __name__ == '__main__':
    GajiKaryawanApp().run()
