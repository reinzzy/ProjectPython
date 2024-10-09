from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager

Config.set('input', 'mouse', 'mouse,disable_multitouch')

Config.set('kivy', 'keyboard_mode', 'system')

class AbsensiScreen(Screen):
    def __init__(self, **kwargs):
        super(AbsensiScreen, self).__init__(**kwargs)

        # Layout utama
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Header perusahaan
        header_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))
        company_label = Label(text='PT. ABADI SELALU', font_size=24, bold=True)
        header_layout.add_widget(company_label)

        layout.add_widget(header_layout)

       

        # Bagian Tabel Absensi
        table_layout = GridLayout(cols=3, size_hint=(1, 0.6), spacing=10)
        table_layout.add_widget(Label(text='Nama', bold=True))
        table_layout.add_widget(Label(text='Tanggal', bold=True))
        table_layout.add_widget(Label(text='Keterangan', bold=True))

        # Data absensi contoh
        absensi_data = [
            {'nama': 'Dendi', 'tanggal': ['✓', '✓', '✓', '✗', '✓', '✓', '✓', '✓', '✓', '✗'], 'sakit': '3x', 'ijin': '1x'},
            {'nama': 'Rival', 'tanggal': ['✗', '✓', '✓', '✓', '✗', '✓', '✗', '✓', '✗', '✗'], 'sakit': '2x', 'ijin': '1x'},
            {'nama': 'Rezaldi', 'tanggal': ['✓', '✓', '✓', '✓', '✓', '✗', '✓', '✓', '✗', '✗'], 'sakit': '1x', 'ijin': '0x'},
            {'nama': 'Zaki', 'tanggal': ['✓', '✗', '✓', '✗', '✗', '✗', '✗', '✗', '✓', '✗'], 'sakit': '4x', 'ijin': '2x'}
        ]

        # Mengisi tabel absensi
        for data in absensi_data:
            table_layout.add_widget(Label(text=data['nama']))
            table_layout.add_widget(Label(text=" ".join(data['tanggal'])))
            table_layout.add_widget(Label(text=f"Sakit: {data['sakit']}, Ijin: {data['ijin']}"))
            
             # Tombol kembali ke main screen
        back_button = Button(text="Kembali ke Main Screen", size_hint=(1, 0.1), on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'