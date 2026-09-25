def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong


print("Tổng của (1, 2, 3) =", tinh_tong(1, 2, 3))
print("Tổng của (5, 10, 15, 20, 25) =", tinh_tong(5, 10, 15, 20, 25))
print("Tổng khi không truyền số nào =", tinh_tong())