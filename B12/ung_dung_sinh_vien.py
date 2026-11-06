import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_sinh_vien as db

DANH_SACH_NGANH = ["Cong nghe thong tin", "Quan tri kinh doanh", "Trac dia - Ban do", "Quan ly dat dai", "Moi truong", "Khac"]

class UngDungSinhVien(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Sinh vien")
        self.geometry("580x480")
        self.resizable(False, False)
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")
        
        tk.Label(khung_nhap, text="Ho va ten:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ten = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ten.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(khung_nhap, text="Diem TB (0-10):").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_diem = tk.Entry(khung_nhap, width=30)
        self.o_nhap_diem.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Nganh hoc:").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_nganh = ttk.Combobox(khung_nhap, values=DANH_SACH_NGANH, width=27, state="readonly")
        self.chon_nganh.current(0)
        self.chon_nganh.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Button(khung_nhap, text="Them sinh vien", command=self.xu_ly_them).grid(row=3, column=0, columnspan=2, pady=10)
        
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)
        self.listbox_sv = tk.Listbox(khung_danh_sach, width=75, height=14)
        self.listbox_sv.pack(side="left", fill="both", expand=True)
        
        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_sv.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sv.config(yscrollcommand=thanh_cuon.set)
        
        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)
        
        tk.Button(khung_nut_thao_tac, text="Xac nhan Dat (Qua mon)", command=self.xu_ly_danh_dau_dat).grid(row=0, column=0, padx=5)
        tk.Button(khung_nut_thao_tac, text="Xoa sinh vien", command=self.xu_ly_xoa).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut_thao_tac, text="Thong ke theo nganh", command=self.xu_ly_thong_ke).grid(row=0, column=2, padx=5)

    def tai_lai_danh_sach(self):
        self.listbox_sv.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_sinh_vien()
        for sv in self.danh_sach_hien_tai:
            id_sv, ho_ten, diem_tb, nganh_hoc, trang_thai = sv
            kq = "[Dat]" if trang_thai == 1 else "[Chua xet]"
            self.listbox_sv.insert(tk.END, f"{kq} {ho_ten} - Diem: {diem_tb} - ({nganh_hoc})")

    def xu_ly_them(self):
        ho_ten = self.o_nhap_ten.get().strip()
        diem_str = self.o_nhap_diem.get().strip()
        nganh_hoc = self.chon_nganh.get()
        
        if ho_ten == "" or diem_str == "":
            messagebox.showerror("Loi", "Vui long nhap day du ho ten va diem trung binh.")
            return
        try:
            diem_tb = float(diem_str)
            if diem_tb < 0 or diem_tb > 10:
                raise ValueError
        except ValueError:
            messagebox.showerror("Loi", "Diem trung binh phai la so tu 0.0 den 10.0!")
            return

        db.them_sinh_vien(ho_ten, diem_tb, nganh_hoc)
        self.o_nhap_ten.delete(0, tk.END)
        self.o_nhap_diem.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", f"Da them sinh vien: {ho_ten}")

    def xu_ly_xoa(self):
        lua_chon = self.listbox_sv.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot sinh vien trong danh sach de xoa.")
            return
        id_sv = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_sinh_vien(id_sv)
        self.tai_lai_danh_sach()

    def xu_ly_danh_dau_dat(self):
        lua_chon = self.listbox_sv.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot sinh vien de xac nhan Dat.")
            return
        id_sv = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.danh_dau_dat(id_sv)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_nganh()
        if not du_lieu_thong_ke:
            messagebox.showinfo("Thong bao", "Chua co du lieu sinh vien de thong ke.")
            return
        cac_nganh = [dong[0] for dong in du_lieu_thong_ke]
        so_luong = [dong[1] for dong in du_lieu_thong_ke]
        
        plt.figure(figsize=(7, 4))
        plt.bar(cac_nganh, so_luong, color="teal")
        plt.title("Thong ke so luong sinh vien theo nganh hoc")
        plt.xlabel("Nganh hoc")
        plt.ylabel("So luong sinh vien")
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    ung_dung = UngDungSinhVien()
    ung_dung.mainloop()