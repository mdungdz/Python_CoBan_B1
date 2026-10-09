import tkinter as tk

# Hàm xử lý khi bấm nút Submit (Lấy dữ liệu từ ô nhập)
def xu_ly_submit():
    ho_ten = entry_ho_ten.get().strip()
    tuoi = entry_tuoi.get().strip()
    email = entry_email.get().strip()
    
    if not ho_ten or not tuoi or not email:
        nhan_ket_qua.config(
            text="Vui long nhap day du thong tin!", 
            fg="red"
        )
    else:
        nhan_ket_qua.config(
            text=f"Da nhan: {ho_ten} - {tuoi} tuoi - {email}", 
            fg="blue"
        )

# Hàm xử lý khi bấm nút Xóa (Yêu cầu mở rộng)
def xu_ly_xoa():
    # .delete(0, tk.END) xóa sạch văn bản từ ký tự đầu (0) đến ký tự cuối (END)
    entry_ho_ten.delete(0, tk.END)
    entry_tuoi.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    # Xóa luôn dòng thông báo kết quả và đưa con trỏ chuột về lại ô Họ tên
    nhan_ket_qua.config(text="")
    entry_ho_ten.focus()

# Khởi tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Form nhap thong tin")
cua_so.geometry("400x300")
cua_so.resizable(False, False)

# 1. Hàng 0: Họ tên
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_ho_ten = tk.Entry(cua_so, width=25)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)

# 2. Hàng 1: Tuổi
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_tuoi = tk.Entry(cua_so, width=25)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)

# 3. Hàng 2: Email
tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(cua_so, width=25)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# 4. Hàng 3: Khung chứa nút bấm (Submit & Xóa) xếp cùng hàng
khung_nut = tk.Frame(cua_so)
khung_nut.grid(row=3, column=0, columnspan=2, pady=15)

nut_submit = tk.Button(khung_nut, text="Submit", width=10, command=xu_ly_submit)
nut_submit.pack(side="left", padx=5)

nut_xoa = tk.Button(khung_nut, text="Xoa", width=10, command=xu_ly_xoa)
nut_xoa.pack(side="left", padx=5)

# 5. Hàng 4: Nhãn hiển thị kết quả
nhan_ket_qua = tk.Label(cua_so, text="", font=("Arial", 11), fg="blue")
nhan_ket_qua.grid(row=4, column=0, columnspan=2, pady=10)

cua_so.mainloop()