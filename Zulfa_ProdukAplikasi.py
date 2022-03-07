import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from  PyQt5.QtWidgets import *

def window_go(): #fungsi untuk menentukan layout window
    #inisialisasi pyqt
    app = QApplication(sys.argv)
    window = QWidget()

    grid = QGridLayout() #Widget untuk membuat grid
    vbox = QVBoxLayout() #Widget untuk membuat layout secara vertikal

    #Judul Form
    tas = QLabel("Form Pemesanan Tas") #menyiapkan label
    tas.setStyleSheet("font-family: forte; font-size: 25px; font: bold;") #setStyleSheet digunakan untuk mengatur style dari label
    tas.setAlignment(Qt.AlignCenter) #setAlignment untuk mengatur align dari label
    toko = QLabel("Toko Zulfa")
    toko.setStyleSheet("font-family: euphemia; font-size: 18px; font: bold;")
    toko.setAlignment(Qt.AlignCenter)

    vbox.addWidget(tas) #menampilkan elemen pada layout vbox
    vbox.addWidget(toko)
    grid.addLayout(vbox,1,1,1,4) #menampilkan elemen pada layout grid

    #form
    nama = QLineEdit(window) #membuat kolom input
    nama2 = QLabel("Nama")
    grid.addWidget(nama2,4,1)
    grid.addWidget(nama,4,2)

    alamat = QLineEdit(window)
    alamat2 = QLabel("Alamat")
    grid.addWidget(alamat2,5,1)
    grid.addWidget(alamat,5,2)

    telp = QLineEdit(window)
    telp.setValidator(QIntValidator()) #membatasi masukan menjadi bilangan bulat
    telp2 = QLabel("No Telpon")
    grid.addWidget(telp2,6,1)
    grid.addWidget(telp,6,2)

    comBox = QComboBox() #menampilkan daftar dropdown item
    merk = QLabel("Merk Tas")
    comBox.addItem("--Pilih Merk--")
    comBox.addItems(["Gucci","Gold","Hermes","Louis Vuitton","Pierre Cardin"]) #dropdown item
    grid.addWidget(merk,7,1)
    grid.addWidget(comBox,7,2)

    spinBox = QSpinBox() #menyajikan pengguna dengan kotak teks yang menampilkan bilangan bulat dengan tombol atas / bawah di sebelah kanannya.
    banyak = QLabel("Banyaknya")
    spinBox.setValue(10) #mengatur angka awal dalam spinbox
    grid.addWidget(banyak,8,1)
    grid.addWidget(spinBox,8,2)

    comBox2 = QComboBox()
    kirim = QLabel("Pengiriman")
    comBox2.addItem("--Pilih Pengiriman--")
    comBox2.addItems(["JNT","JNE","Pos"])
    grid.addWidget(kirim,9,1)
    grid.addWidget(comBox2,9,2)

    bayar = QLabel("Pembayaran")
    cod = QRadioButton("COD") #menampilkan tombol yang dapat dipilih dengan label teks
    indomart = QRadioButton("Indomart/Alfamart")
    tfBank = QRadioButton("Transfer Bank")
    grid.addWidget(bayar,10,1)
    grid.addWidget(cod,10,2)
    grid.addWidget(indomart,11,2)
    grid.addWidget(tfBank,12,2)

    #Daftar Harga
    gBox = QGroupBox() #membuat layout grup box
    grid.addWidget(gBox,1,7,25,35)
    vbox = QVBoxLayout()
    hbox = QHBoxLayout()
    gBox.setLayout(vbox) #menampilkan layout grup box
    gBox.setStyleSheet("background-color: pink;")

    harga = QLabel("Daftar Harga Tas")
    harga.setStyleSheet("font-family: forte; font-size: 25px; font: bold;")
    harga.setAlignment(Qt.AlignCenter)

    gucci = QLabel("Gucci")
    hargaG = QLabel("Rp 6.947.736,00")
    hbox1 = QHBoxLayout()
    hbox1.addWidget(gucci)
    hbox1.addWidget(hargaG)

    gold = QLabel("Gold")
    hargaGo = QLabel("Rp 945.500,00")
    hbox2 = QHBoxLayout()
    hbox2.addWidget(gold)
    hbox2.addWidget(hargaGo)

    hermes = QLabel("Hermes")
    hargaH = QLabel("Rp 57.000.000,00")
    hbox3 = QHBoxLayout()
    hbox3.addWidget(hermes)
    hbox3.addWidget(hargaH)

    louis = QLabel("Louis Vuitton")
    hargaL = QLabel("Rp 28.750.000,00")
    hbox4 = QHBoxLayout()
    hbox4.addWidget(louis)
    hbox4.addWidget(hargaL)

    piere = QLabel("Pierre Cardin")
    hargaP = QLabel("Rp 3.499.000,00")
    hbox5 = QHBoxLayout()
    hbox5.addWidget(piere)
    hbox5.addWidget(hargaP)

    #menampilkan daftar harga
    vbox.addWidget(harga)
    vbox.addLayout(hbox)
    vbox.addLayout(hbox1)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)
    vbox.addLayout(hbox4)
    vbox.addLayout(hbox5)


    #Tombol Button
    hbox = QHBoxLayout()
    button = QPushButton("Checkout")
    hbox.addWidget(button)
    grid.addLayout(hbox,13,1,13,2)

    button.clicked.connect(checkout) #menghubungkan ke slot(fungsi checkout)

    #menentukan ukuran window + title dan menampilkan
    window.setGeometry(300,150,700,380)
    window.setLayout(grid)
    window.setWindowTitle("Toko Tas Zulfa")
    window.show()
    sys.exit(app.exec_())

def checkout(): #fungsi untuk membuat alert pesan box
    msg = QMessageBox() #widget membuat pesan box / alert
    msg.setInformativeText("Terimakasih telah berlangganan di toko kami") #mengatur tulisan dari infromasi
    msg.setWindowTitle("Toko Tas Zulfa")
    msg.exec_()

if __name__ == '__main__':
    window_go()
