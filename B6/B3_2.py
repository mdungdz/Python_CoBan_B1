def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Họ tên: {ho_ten} - Tuổi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"  {khoa}: {gia_tri}")


in_thong_tin("Nguyễn Văn A", 20, lop="CNTT01", que_quan="Hà Nội")
in_thong_tin("Trần Thị B", 21, email="b@example.com")