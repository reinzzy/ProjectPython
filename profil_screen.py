from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App

class ProfilScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfilScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        profile_label = Label(text="Profil Admin", font_size=32, size_hint=(1, 0.2))
        layout.add_widget(profile_label)
        
        back_button = Button(text="Back", size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        logout_button = Button(text="Logout", size_hint=(1, 0.2))
        logout_button.bind(on_press=self.logout)
        layout.add_widget(logout_button)
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = 'main'  # Kembali ke MainScreen
    
    def logout(self, instance):
        self.manager.current = 'login'  # Kembali ke LoginScreen