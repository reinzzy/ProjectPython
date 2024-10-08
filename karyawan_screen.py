from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

# Screen untuk pendaftaran karyawan
class EmployeeRegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Form input karyawan
        self.first_name_input = TextInput(hint_text="Nama Depan", multiline=False)
        self.last_name_input = TextInput(hint_text="Nama Tengah/Belakang", multiline=False)
        self.job_input = TextInput(hint_text="Job Desk", multiline=False)
        self.status_input = TextInput(hint_text="Status", multiline=False)
        self.position_input = TextInput(hint_text="Jabatan", multiline=False)

        # Tombol untuk unggah foto
        self.photo_button = Button(text="Upload Foto (max 200KB)")
        self.photo_button.bind(on_press=self.show_filechooser)
        self.photo_path = None

        # Tombol submit
        input_button = Button(text="INPUT", size_hint=(1, 0.2))
        input_button.bind(on_press=self.submit_data)

        # Menambahkan widget ke layout
        layout.add_widget(Label(text="PT. ABADI SELALU", font_size=24))
        layout.add_widget(self.first_name_input)
        layout.add_widget(self.last_name_input)
        layout.add_widget(self.job_input)
        layout.add_widget(self.status_input)
        layout.add_widget(self.position_input)
        layout.add_widget(self.photo_button)
        layout.add_widget(input_button)

        self.add_widget(layout)

    # Fungsi untuk membuka file chooser
    def show_filechooser(self, instance):
        filechooser = FileChooserIconView()
        popup = Popup(title="Pilih Foto", content=filechooser, size_hint=(0.9, 0.9))

        filechooser.bind(on_selection=lambda x: self.select_photo(x, popup))
        popup.open()

    def select_photo(self, filechooser, popup):
        if filechooser.selection:
            self.photo_path = filechooser.selection[0]
        popup.dismiss()

    # Fungsi untuk submit data dan berpindah ke layar daftar karyawan
    def submit_data(self, instance):
        first_name = self.first_name_input.text
        last_name = self.last_name_input.text
        job = self.job_input.text
        status = self.status_input.text
        position = self.position_input.text

        if first_name and last_name and job and status and position:
            # Tambahkan data ke daftar karyawan (layar kedua)
            employee_list_screen = self.manager.get_screen('employee_list')
            employee_list_screen.add_employee(
                first_name + " " + last_name, job, status
            )
            self.manager.current = 'employee_list'
        else:
            popup = Popup(title="Error", content=Label(text="Semua kolom wajib diisi!"), size_hint=(0.6, 0.4))
            popup.open()

# Screen untuk daftar karyawan
class EmployeeListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.layout.add_widget(Label(text="DAFTAR KARYAWAN", font_size=24))

        # Membuat header
        header_layout = GridLayout(cols=3, size_hint_y=None, height=30)
        header_layout.add_widget(Label(text="Nama", bold=True))
        header_layout.add_widget(Label(text="Job Desk", bold=True))
        header_layout.add_widget(Label(text="Status", bold=True))
        self.layout.add_widget(header_layout)

        self.add_widget(self.layout)

    # Fungsi untuk menambahkan karyawan ke daftar
    def add_employee(self, name, job, status):
        # Membuat baris untuk karyawan
        row_layout = GridLayout(cols=3, size_hint_y=None, height=30)
        row_layout.add_widget(Label(text=name))
        row_layout.add_widget(Label(text=job))
        row_layout.add_widget(Label(text=status))
        self.layout.add_widget(row_layout)
