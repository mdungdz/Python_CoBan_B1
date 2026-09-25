def gioi_thieu(ten, tuoi=18, lop="Chưa rõ"):
    print(f"Tên: {ten} - Tuổi: {tuoi} - Lớp: {lop}")


gioi_thieu("An")                                  # dùng hết giá trị mặc định
gioi_thieu("Bình", 20)                            # ghi đè tuổi
gioi_thieu("Chi", lop="CNTT01")                   # dùng tham số từ khóa, bỏ qua tuổi
gioi_thieu(ten="Dũng", lop="CNTT02", tuoi=19)     # thứ tự tham số từ khóa có thể đảo lộn