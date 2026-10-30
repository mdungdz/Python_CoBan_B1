import pandas as pd
import matplotlib.pyplot as plt

# Đọc file dữ liệu để tạo biến df
df = pd.read_csv("diem_sinh_vien.csv")

# Phần code vẽ biểu đồ của thầy
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
plt.figure(figsize=(6, 4))
plt.bar(diem_trung_binh_mon.index, diem_trung_binh_mon.values, color="skyblue")
plt.title("Diem trung binh theo mon hoc")
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")
plt.savefig("bieu_do_cot.png")
plt.show()