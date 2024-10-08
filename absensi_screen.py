from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

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

        # Bagian Input Tanggal
        date_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        date_layout.add_widget(Label(text='Day'))
        self.day_input = TextInput(hint_text='DD', multiline=False)
        date_layout.add_widget(self.day_input)

        date_layout.add_widget(Label(text='Month'))
        self.month_input = TextInput(hint_text='MM', multiline=False)
        date_layout.add_widget(self.month_input)

        date_layout.add_widget(Label(text='Year'))
        self.year_input = TextInput(hint_text='YYYY', multiline=False)
        date_layout.add_widget(self.year_input)

        # Tombol search
        search_button = Button(text='Search')
        date_layout.add_widget(search_button)

        layout.add_widget(date_layout)

        # Bagian Tabel Absensi
        table_layout = GridLayout(cols=3, size_hint=(1, 0.6), spacing=10)
        table_layout.add_widget(Label(text='Nama', bold=True))
        table_layout.add_widget(Label(text='Tanggal', bold=True))
        table_layout.add_widget(Label(text='Ket', bold=True))

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
