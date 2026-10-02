# ==============================================================================
# BÀI TẬP VẬN DỤNG: BẮT BUỘC NHẬP SỐ NGUYÊN DƯƠNG HỢP LỆ VỚI TRY-EXCEPT VÀ WHILE
# ==============================================================================

def nhap_so_luong_hop_le():
    while True:
        try:
            so_luong = int(input("Nhap so luong (so nguyen duong): "))
            if so_luong > 0:
                return so_luong
            print("So luong phai lon hon 0, vui long nhap lai.\n")
        except ValueError:
            print("Du lieu khong hop le, vui long nhap lai mot so nguyen.\n")

# Luồng chính của chương trình
def main():
    print("--- CHƯƠNG TRÌNH XÁC NHẬN SỐ LƯỢNG HÀNG HÓA ---")
    so_luong_nhap = nhap_so_luong_hop_le()
    print("-" * 45)
    print("So luong hop le da nhap:", so_luong_nhap)

if __name__ == "__main__":
    main()