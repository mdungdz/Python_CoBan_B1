import tkinter as tk
from tkinter import messagebox


def bam_nut(ky_tu):
    entry_man_hinh.insert(tk.END, ky_tu)


def xoa_het():
    entry_man_hinh.delete(0, tk.END)


def xoa_mot_ky_tu():
    noi_dung = entry_man_hinh.get()
    xoa_het()
    entry_man_hinh.insert(0, noi_dung[:-1])


def tinh_ket_qua():
    bieu_thuc = entry_man_hinh.get().strip()
    if bieu_thuc == "":
        return
    try:
        ket_qua = eval(bieu_thuc)
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0.")
        return
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le.")
        return
    xoa_het()
    entry_man_hinh.insert(0, str(ket_qua))


cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.resizable(False, False)

# Màn hình hiển thị biểu thức / kết quả
entry_man_hinh = tk.Entry(cua_so, font=("Arial", 20), justify="right", width=16)
entry_man_hinh.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Bàn phím số và phép tính
ban_phim = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

for hang, cac_nut in enumerate(ban_phim, start=1):
    for cot, ky_tu in enumerate(cac_nut):
        if ky_tu == "=":
            lenh = tinh_ket_qua
        else:
            lenh = lambda kt=ky_tu: bam_nut(kt)
        tk.Button(cua_so, text=ky_tu, width=5, height=2, font=("Arial", 14),
                  command=lenh).grid(row=hang, column=cot, padx=3, pady=3)

# Hàng cuối: nút C (xóa hết) và Xoa lui
tk.Button(cua_so, text="C", width=11, height=2, font=("Arial", 14),
          command=xoa_het).grid(row=5, column=0, columnspan=2, padx=3, pady=8)
tk.Button(cua_so, text="Xoa lui", width=11, height=2, font=("Arial", 14),
          command=xoa_mot_ky_tu).grid(row=5, column=2, columnspan=2, padx=3, pady=8)

cua_so.mainloop()