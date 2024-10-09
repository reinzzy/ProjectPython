from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.config import Config

Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('kivy', 'keyboard_mode', 'system')

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=40, spacing=10)

        title = Label(text="LOGIN", font_size=32, bold=True)
        layout.add_widget(title)

        self.username = TextInput(hint_text="Username", multiline=False)
        layout.add_widget(self.username)

        self.password = TextInput(hint_text="Password", password=True, multiline=False)
        layout.add_widget(self.password)

        # Tombol Login
        self.login_button = Button(text="LOGIN", size_hint=(1, 0.2))
        self.login_button.bind(on_press=self.login)
        layout.add_widget(self.login_button)

        self.add_widget(layout)

    # Fungsi untuk login
    def login(self, instance):
        # Periksa username dan password
        if self.username.text == "admin" and self.password.text == "admin":
            self.show_popup("Login Berhasil", "Selamat datang!")
            self.manager.current = 'main'  # Jika benar, alihkan ke halaman utama
        else:
            self.show_popup("Login Gagal", "Username atau password salah!")

    # Fungsi untuk menampilkan popup
    def show_popup(self, title, message):
        # Layout dari popup
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        popup_label = Label(text=message)
        popup_layout.add_widget(popup_label)

        # Tombol OK untuk menutup popup
        ok_button = Button(text="OK", size_hint=(1, 0.2))
        popup_layout.add_widget(ok_button)

        # Membuat popup
        popup = Popup(title=title, content=popup_layout, size_hint=(0.6, 0.4))

        # Fungsi untuk menutup popup saat OK ditekan
        ok_button.bind(on_press=popup.dismiss)

        # Menampilkan popup
        popup.open()
