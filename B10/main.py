import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("form_dang_nhap.ui", self)  # Nạp giao diện từ file .ui
        
        # Kết nối signal - slot cho nút đăng nhập (tên widget lấy từ objectName đã đặt trong Designer)
        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text()
        mat_khau = self.o_nhap_mat_khau.text()
        
        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Lỗi", "Vui lòng nhập đầy đủ tài khoản và mật khẩu.")
            return
            
        QMessageBox.information(self, "Thành công", f"Xin chào {tai_khoan}, đăng nhập thành công!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec_())