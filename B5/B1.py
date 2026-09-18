# Bài tập 1.1: Kiểm tra tuổi trưởng thành và điều kiện đăng ký xe máy (if, if-else)
tuoi = 20
if tuoi >= 18:
    print("Da du tuoi truong thanh")

if tuoi >= 18:
    print("Duoc phep dang ky xe may")
else:
    print("Chua du tuoi")


# Bài tập 1.2: Xếp loại học lực theo thang điểm (if-elif-else)
diem = 7.2
if diem >= 8.0:
    print("Xep loai: Gioi")
elif diem >= 6.5:
    print("Xep loai: Kha")
elif diem >= 5.0:
    print("Xep loai: Trung binh")
else:
    print("Xep loai: Yeu")


# Bài tập 1.3: Kiểm tra điều kiện lái xe (Câu lệnh điều kiện lồng nhau)
tuoi = 17
co_giay_phep = False
if tuoi >= 18:
    if co_giay_phep:
        print("Duoc phep lai xe")
    else:
        print("Du tuoi nhung chua co giay phep")
else:
    print("Chua du tuoi lai xe")

# Bài tập 1.4: Lọc kết quả và tính giá trị tuyệt đối (Biểu thức điều kiện rút gọn)
diem = 4.5
ket_qua = "Dat" if diem >= 5.0 else "Khong dat"
print(ket_qua)

so = -7
tri_tuyet_doi = so if so >= 0 else -so
print(tri_tuyet_doi)