from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager

class AbsensiScreen(Screen):
    def __init__(self, **kwargs):
        super(AbsensiScreen, self).__init__(**kwargs)

        # Layout utama
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Header perusahaan dengan tombol "Kembali" di pojok kiri atas
        header_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))

        # Tombol kembali
        back_button = Button(text='< Kembali', size_hint=(0.2, 0.2), on_press=self.go_back)
        header_layout.add_widget(back_button)

        # Label perusahaan di bagian tengah header
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

        layout.add_widget(table_layout)

        self.add_widget(layout)

    def go_back(self, instance):
        # Mengubah layar kembali ke MainScreen
        self.manager.current = 'main'

# ScreenManager setup (sebagai contoh)
screen_manager = ScreenManager()
screen_manager.add_widget(AbsensiScreen(name='absensi'))
