from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

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

    def login(self, instance):
        # Periksa username dan password
        if self.username.text == "admin" and self.password.text == "admin":
            # Jika benar, alihkan ke halaman utama
            self.manager.current = 'main'
        else:
            print("Login failed!")
