from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.app import App

class ImageButton(ButtonBehavior, Image):
    pass

class MainScreen(Screen):
    def _init_(self, **kwargs):
        super(MainScreen, self)._init_(**kwargs)

        # Layout utama
        layout = BoxLayout(orientation='vertical')

        # Bagian Header
        header = BoxLayout(orientation='horizontal', size_hint=(1, 0.15), padding=10)
        
        # Nama Perusahaan dan Greeting
        company_label = Label(text="PT. ABADI SELALU", font_size=24, bold=True)
        greeting_label = Label(text="Hi, ADMIN1", size_hint_x=0.3, halign='right', valign='middle')

        # Ikon profil
        profile_icon = ImageButton(source='picture/profile_icon.png', size_hint=(0.1, 1))
        profile_icon.bind(on_press=self.go_to_profile)  # Bind ke fungsi perpindahan layar
        
        header.add_widget(greeting_label)
        header.add_widget(company_label)
        header.add_widget(profile_icon)
        layout.add_widget(header)

        # Bagian Chart
        chart_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.4))

        chart_title = Label(text="[color=6495ED]Data Karyawan Yang Sudah Ter-Rekap[/color]", markup=True, font_size=16, halign='center')
        chart = BoxLayout(orientation='horizontal')

        # Widget "Sudah" dan "Belum" untuk Chart
        chart_left = Widget(size_hint_x=0.7)  # Widget kiri untuk "Sudah"
        chart_right = Widget(size_hint_x=0.3)  # Widget kanan untuk "Belum"

        # Buat grafik dengan menggunakan Canvas
        with chart_left.canvas:
            Color(0.39, 0.58, 0.93, 1)  # Warna biru untuk "Sudah"
            self.chart_left_rect = Rectangle(size=chart_left.size, pos=chart_left.pos)

        with chart_right.canvas:
            Color(0.94, 0.5, 0.5, 1)  # Warna merah untuk "Belum"
            self.chart_right_rect = Rectangle(size=chart_right.size, pos=chart_right.pos)

        chart.add_widget(chart_left)
        chart.add_widget(chart_right)

        chart_label_layout = BoxLayout(orientation='horizontal')
        sudah_label = Label(text="Sudah", size_hint_x=0.7, halign='center')
        belum_label = Label(text="Belum", size_hint_x=0.3, halign='center')
        chart_label_layout.add_widget(sudah_label)
        chart_label_layout.add_widget(belum_label)

        chart_layout.add_widget(chart_title)
        chart_layout.add_widget(chart)
        chart_layout.add_widget(chart_label_layout)

        layout.add_widget(chart_layout)

        # Bagian Menu Tombol
        menu_layout = GridLayout(cols=1, size_hint=(1, 0.45), spacing=10, padding=[10, 10, 10, 20])

        absensi_button = Button(text="ABSENSI KARYAWAN", font_size=16)
        absensi_button.bind(on_press=self.go_to_absensi) 

        daftar_karyawan_button = Button(text="DAFTAR KARYAWAN", font_size=16)
        daftar_gaji_button = Button(text="DAFTAR GAJI KARYAWAN", font_size=16)
        cek_gaji_button = Button(text="CEK DATA GAJI KARYAWAN", font_size=16)

        menu_layout.add_widget(absensi_button)
        menu_layout.add_widget(daftar_karyawan_button)
        menu_layout.add_widget(daftar_gaji_button)
        menu_layout.add_widget(cek_gaji_button)

        layout.add_widget(menu_layout)

        self.add_widget(layout)

        # Bind ukuran widget ke fungsi resize agar grafik disesuaikan
        chart_left.bind(size=self.update_chart_left, pos=self.update_chart_left)
        chart_right.bind(size=self.update_chart_right, pos=self.update_chart_right)

    def go_to_profile(self, instance):
        self.manager.current = 'profil'  # Pastikan ini sesuai dengan nama yang diberikan saat layar ditambahkan

    def go_to_absensi(self, instance):
        self.manager.current = 'absensi'

    def update_chart_left(self, instance, value):
        self.chart_left_rect.size = instance.size
        self.chart_left_rect.pos = instance.pos

    def update_chart_right(self, instance, value):
        self.chart_right_rect.size = instance.size
        self.chart_right_rect.pos = instance.pos