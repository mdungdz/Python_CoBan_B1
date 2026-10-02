# ==============================================================================
# ĐỒ ÁN MÔN HỌC: QUẢN LÝ SINH VIÊN MINI
# Ngôn ngữ: Python 3
# Kỹ thuật: List, Dictionary, Loop, Function, Try-Except
# ==============================================================================

# Dữ liệu khởi tạo ban đầu
danh_sach_sv = [
    {"ma_sv": "SV01", "ho_ten": "Nguyen Manh Dung", "toan": 8.5, "ly": 7.0, "hoa": 9.0, "dtb": 8.17, "xep_loai": "Gioi"},
    {"ma_sv": "SV02", "ho_ten": "Tran Thi B", "toan": 6.0, "ly": 6.5, "hoa": 7.0, "dtb": 6.50, "xep_loai": "Kha"},
    {"ma_sv": "SV03", "ho_ten": "Le Van C", "toan": 4.0, "ly": 5.0, "hoa": 4.5, "dtb": 4.50, "xep_loai": "Yeu"}
]

def tinh_dtb_va_xep_loai(toan, ly, hoa):
    """Tính điểm trung bình và trả về xếp loại"""
    dtb = round((toan + ly + hoa) / 3, 2)
    if dtb >= 8.0:
        xep_loai = "Gioi"
    elif dtb >= 6.5:
        xep_loai = "Kha"
    elif dtb >= 5.0:
        xep_loai = "Trung binh"
    else:
        xep_loai = "Yeu"
    return dtb, xep_loai

def nhap_diem_hop_le(ten_mon):
    """Hàm nhập điểm an toàn bằng try-except (bắt buộc từ 0 đến 10)"""
    while True:
        try:
            diem = float(input(f"Nhap diem {ten_mon} (0 - 10): "))
            if 0.0 <= diem <= 10.0:
                return diem
            print("-> Loi: Diem phai nam trong khoang tu 0 den 10. Vui long nhap lai!")
        except ValueError:
            print("-> Loi: Du lieu khong hop le! Vui long nhap mot so thuc.")

def tim_sv_theo_ma(ma_sv):
    """Hàm bổ trợ tìm sinh viên trong danh sách theo Mã SV"""
    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None

def hien_thi_danh_sach():
    """1. Hiển thị danh sách toàn bộ sinh viên"""
    print("\n" + "=" * 75)
    print(f"{'Ma SV':<8}{'Ho va Ten':<20}{'Toan':<8}{'Ly':<8}{'Hoa':<8}{'DTB':<8}{'Xep loai':<10}")
    print("-" * 75)
    if not danh_sach_sv:
        print("Danh sach hien tai dang trong!")
    else:
        for sv in danh_sach_sv:
            print(f"{sv['ma_sv']:<8}{sv['ho_ten']:<20}{sv['toan']:<8.1f}{sv['ly']:<8.1f}"
                  f"{sv['hoa']:<8.1f}{sv['dtb']:<8.2f}{sv['xep_loai']:<10}")
    print("=" * 75)

def them_sinh_vien():
    """2. Thêm sinh viên mới"""
    print("\n--- THEM SINH VIEN MOI ---")
    ma_sv = input("Nhap ma sinh vien (vd: SV04): ").strip().upper()
    if tim_sv_theo_ma(ma_sv) is not None:
        print(f"-> Loi: Ma sinh vien {ma_sv} da ton tai trong he thong!")
        return

    ho_ten = input("Nhap ho va ten sinh vien: ").strip().title()
    toan = nhap_diem_hop_le("Toan")
    ly = nhap_diem_hop_le("Ly")
    hoa = nhap_diem_hop_le("Hoa")

    dtb, xep_loai = tinh_dtb_va_xep_loai(toan, ly, hoa)

    danh_sach_sv.append({
        "ma_sv": ma_sv, "ho_ten": ho_ten,
        "toan": toan, "ly": ly, "hoa": hoa,
        "dtb": dtb, "xep_loai": xep_loai
    })
    print(f"-> Da them sinh vien {ho_ten} ({ma_sv}) thanh cong!")

def cap_nhat_sinh_vien():
    """3. Cập nhật thông tin sinh viên"""
    print("\n--- CAP NHAT THONG TIN SINH VIEN ---")
    ma_sv = input("Nhap ma sinh vien can sua: ").strip().upper()
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien voi ma {ma_sv}!")
        return

    print(f"Dang sua thong tin cho sinh vien: {sv['ho_ten']}")
    ho_ten_moi = input(f"Nhap ho ten moi (De trong neu giu nguyen '{sv['ho_ten']}'): ").strip().title()
    if ho_ten_moi:
        sv["ho_ten"] = ho_ten_moi

    sua_diem = input("Ban co muon nhap lai diem khong? (y/n): ").strip().lower()
    if sua_diem == 'y':
        sv["toan"] = nhap_diem_hop_le("Toan")
        sv["ly"] = nhap_diem_hop_le("Ly")
        sv["hoa"] = nhap_diem_hop_le("Hoa")
        sv["dtb"], sv["xep_loai"] = tinh_dtb_va_xep_loai(sv["toan"], sv["ly"], sv["hoa"])

    print(f"-> Cap nhat thong tin sinh vien {ma_sv} thanh cong!")

def xoa_sinh_vien():
    """4. Xóa sinh viên"""
    print("\n--- XOA SINH VIEN ---")
    ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien voi ma {ma_sv}!")
        return

    danh_sach_sv.remove(sv)
    print(f"-> Da xoa sinh vien {sv['ho_ten']} ({ma_sv}) khoi danh sach!")

def tim_kiem_sinh_vien():
    """5. Tìm kiếm sinh viên"""
    print("\n--- TIM KIEM SINH VIEN ---")
    ma_sv = input("Nhap ma sinh vien can tim: ").strip().upper()
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien voi ma {ma_sv}!")
        return

    print("\nTHONG TIN SINH VIEN TIM THAY:")
    print(f"Ma SV     : {sv['ma_sv']}")
    print(f"Ho va ten : {sv['ho_ten']}")
    print(f"Diem Toan : {sv['toan']}")
    print(f"Diem Ly   : {sv['ly']}")
    print(f"Diem Hoa  : {sv['hoa']}")
    print(f"Diem TB   : {sv['dtb']}")
    print(f"Xep loai  : {sv['xep_loai']}")

def thong_ke():
    """6. Thống kê chung"""
    print("\n--- THONG KE CHUNG ---")
    tong_sv = len(danh_sach_sv)
    if tong_sv == 0:
        print("Chua co sinh vien nao trong he thong!")
        return

    tong_dtb = sum(sv["dtb"] for sv in danh_sach_sv)
    dtb_lop = round(tong_dtb / tong_sv, 2)

    gioi = sum(1 for sv in danh_sach_sv if sv["xep_loai"] == "Gioi")
    kha = sum(1 for sv in danh_sach_sv if sv["xep_loai"] == "Kha")
    tb = sum(1 for sv in danh_sach_sv if sv["xep_loai"] == "Trung binh")
    yeu = sum(1 for sv in danh_sach_sv if sv["xep_loai"] == "Yeu")

    print(f"Tong so sinh vien      : {tong_sv}")
    print(f"Diem trung binh chung  : {dtb_lop}")
    print(f"So sinh vien Gioi      : {gioi} ({gioi/tong_sv*100:.1f}%)")
    print(f"So sinh vien Kha       : {kha} ({kha/tong_sv*100:.1f}%)")
    print(f"So sinh vien Trung binh: {tb} ({tb/tong_sv*100:.1f}%)")
    print(f"So sinh vien Yeu       : {yeu} ({yeu/tong_sv*100:.1f}%)")

def hien_thi_menu():
    print("\n===== HE THONG QUAN LY SINH VIEN MINI =====")
    print("1. Hien thi danh sach sinh vien")
    print("2. Them sinh vien moi")
    print("3. Cap nhat thong tin sinh vien")
    print("4. Xoa sinh vien")
    print("5. Tim kiem sinh vien")
    print("6. Thong ke")
    print("0. Thoat chuong trinh")

def main():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban (0-6): ").strip()
        if lua_chon == "1":
            hien_thi_danh_sach()
        elif lua_chon == "2":
            them_sinh_vien()
        elif lua_chon == "3":
            cap_nhat_sinh_vien()
        elif lua_chon == "4":
            xoa_sinh_vien()
        elif lua_chon == "5":
            tim_kiem_sinh_vien()
        elif lua_chon == "6":
            thong_ke()
        elif lua_chon == "0":
            print("Cam on ban da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai (0-6).")

if __name__ == "__main__":
    main()