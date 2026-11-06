import sqlite3
TEN_FILE_CSDL = "sinh_vien.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS sinh_vien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ho_ten TEXT NOT NULL,
            diem_tb REAL NOT NULL,
            nganh_hoc TEXT NOT NULL,
            trang_thai INTEGER NOT NULL DEFAULT 0
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_sinh_vien(ho_ten, diem_tb, nganh_hoc):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    # Mặc định trang_thai = 0 (Chưa xét/Chưa đạt), nếu điểm >= 5.0 có thể bấm nút xét Đạt
    con_tro.execute(
        "INSERT INTO sinh_vien (ho_ten, diem_tb, nganh_hoc, trang_thai) VALUES (?, ?, ?, 0)",
        (ho_ten, diem_tb, nganh_hoc)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_sinh_vien():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ho_ten, diem_tb, nganh_hoc, trang_thai FROM sinh_vien ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_sinh_vien(id_sv):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM sinh_vien WHERE id = ?", (id_sv,))
    ket_noi.commit()
    ket_noi.close()

def danh_dau_dat(id_sv):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("UPDATE sinh_vien SET trang_thai = 1 WHERE id = ?", (id_sv,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_nganh():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT nganh_hoc, COUNT(*) FROM sinh_vien GROUP BY nganh_hoc")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua