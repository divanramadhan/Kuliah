import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QDateEdit
from PyQt5.QtCore import QDate

class Program(QWidget):
    def __init__(self):
        super().__init__()
        self.catatanKu()

    def catatanKu(self):
        # Membuat tata letak utama
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Membuat tata letak untuk bagian kanan
        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

        # Membuat label dan tempat untuk menampilkan catatan
        label_catatan = QLabel("Catatan:")
        self.catatan = QTextEdit()
        self.catatan.setReadOnly(True)
        right_layout.addWidget(label_catatan)
        right_layout.addWidget(self.catatan)

        # Membuat tata letak untuk bagian kiri
        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)

        # Membuat label dan form untuk memasukkan catatan
        label_input_catatan = QLabel("Masukkan Catatan:")
        self.input_catatan = QLineEdit()
        left_layout.addWidget(label_input_catatan)
        left_layout.addWidget(self.input_catatan)

        # Membuat date edit untuk memilih tanggal
        label_tanggal = QLabel("Pilih tanggal:")
        self.input_tanggal = QDateEdit()
        self.input_tanggal.setCalendarPopup(True)
        self.input_tanggal.setDate(QDate.currentDate())  # Untuk set tanggal default ke tanggal sekarang
        left_layout.addWidget(label_tanggal)
        left_layout.addWidget(self.input_tanggal)

        # Membuat tombol untuk menyimpan catatan
        tombol_simpan = QPushButton("Simpan")
        tombol_simpan.clicked.connect(self.saveText)
        left_layout.addWidget(tombol_simpan)

        # Menampilkan program CatatanKu
        self.setWindowTitle("CatatanKu")
        self.setGeometry(100, 100, 400, 300)
        self.show()

    def saveText(self):
        # Mengambil teks dari tempat kita memasukkan catatan [baris 30]
        text = self.input_catatan.text()

        # Mengambil tanggal dari tempat kita mengambil tanggal [baris 36]
        date = self.input_tanggal.date().toString("dd/MM/yyyy")

        # Menyimpan catatan dan tanggal untuk ditampilkan
        self.catatan.append(f"Catatan: {text}\nTanggal: {date}\n")

        # Mengosongkan tempat memasukkan catatan setelah catatan dimasukkan ke data
        self.input_catatan.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Program()
    sys.exit(app.exec_())