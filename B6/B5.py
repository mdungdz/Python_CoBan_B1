danh_sach_so = [1, 2, 3, 4, 5]

# ===== Bài 5.1 – map() với lambda =====
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))
print("Bình phương:", binh_phuong)


# ===== Bài 5.2 – filter() với lambda =====
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print("Số chẵn:", so_chan)


# ===== Bài 5.3 – sorted() với lambda =====
danh_sach_sv = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Bình", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2},
]

sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["diem"])
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["diem"], reverse=True)

print("--- Tăng dần ---")
for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])

print("--- Giảm dần ---")
for sv in sap_xep_giam_dan:
    print(sv["ten"], "-", sv["diem"])