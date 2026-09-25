def in_loi_chao(ten):
    print(f"Xin chào, {ten}!")
    return  # hàm không trả về giá trị (trả về None)


def chia_lay_thuong_du(a, b):
    return a // b, a % b  # trả về nhiều giá trị qua tuple


in_loi_chao("An")

thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thương: {thuong}, dư: {du}")