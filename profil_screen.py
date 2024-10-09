from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.config import Config

Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('kivy', 'keyboard_mode', 'system')

class ProfilScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfilScreen, self).__init__(**kwargs)
        
        # Layout utama vertikal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Layout horizontal untuk tombol back di pojok kiri atas
        top_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        
        back_button = Button(text="< Back", size_hint=(0.2, 1))
        back_button.bind(on_press=self.go_back)
        top_layout.add_widget(back_button)

        layout.add_widget(top_layout)
        
        # Label Profil Admin
        profile_label = Label(text="Profil Admin", font_size=32, size_hint=(1, 0.2))
        layout.add_widget(profile_label)
        
        # Tombol Logout
        logout_button = Button(text="Logout", size_hint=(1, 0.2))
        logout_button.bind(on_press=self.show_logout_confirmation)
        layout.add_widget(logout_button)
        
        self.add_widget(layout)

    # Fungsi untuk kembali ke layar utama (MainScreen)
    def go_back(self, instance):
        self.manager.current = 'main'
    
    # Fungsi untuk menampilkan popup konfirmasi logout
    def show_logout_confirmation(self, instance):
        # Membuat konten popup dengan pesan dan dua tombol
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        confirmation_label = Label(text="Apakah Anda yakin ingin logout?")
        popup_layout.add_widget(confirmation_label)

        # Layout untuk tombol "Ya" dan "Tidak"
        button_layout = BoxLayout(orientation='horizontal', spacing=20)

        yes_button = Button(text="Ya", size_hint=(0.5, 1))
        no_button = Button(text="Tidak", size_hint=(0.5, 1))

        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)
        popup_layout.add_widget(button_layout)

        # Membuat popup
        popup = Popup(title="Konfirmasi Logout", content=popup_layout, size_hint=(0.6, 0.4))

        # Fungsi jika tombol "Ya" ditekan
        yes_button.bind(on_press=lambda x: self.logout(popup))

        # Fungsi jika tombol "Tidak" ditekan
        no_button.bind(on_press=popup.dismiss)

        # Menampilkan popup
        popup.open()
    
    # Fungsi untuk logout dan kembali ke layar login
    def logout(self, popup):
        popup.dismiss()  # Menutup popup
        self.manager.current = 'login'  # Kembali ke layar login

# ScreenManager setup (contoh)
class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ProfilScreen(name='profil'))
        sm.add_widget(Screen(name='main'))  # MainScreen placeholder
        sm.add_widget(Screen(name='login'))  # LoginScreen placeholder
        return sm

if __name__ == '__main__':
    TestApp().run()
