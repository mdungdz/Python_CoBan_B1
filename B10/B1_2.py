import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout

class ViDuGridLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vi du QGridLayout")
        self.resize(300, 200)
        
        layout = QGridLayout()
        
        # Thêm các thành phần vào vị trí (hàng, cột) trong lưới
        layout.addWidget(QLabel("Ho ten:"), 0, 0)  # Hàng 0, Cột 0
        layout.addWidget(QLabel("Tuoi:"), 1, 0)     # Hàng 1, Cột 0
        layout.addWidget(QPushButton("Dong y"), 2, 0) # Hàng 2, Cột 0
        layout.addWidget(QPushButton("Huy"), 2, 1)    # Hàng 2, Cột 1
        
        self.setLayout(layout)

app = QApplication(sys.argv)
cua_so = ViDuGridLayout()
cua_so.show()
sys.exit(app.exec_())