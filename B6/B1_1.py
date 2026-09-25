def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def bscnn(a, b):
    return a * b // uscln(a, b)


def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n


# ===== Gọi thử uscln và bscnn với 3 bộ dữ liệu =====
print("UCLN(24, 36) =", uscln(24, 36))
print("BSCNN(24, 36) =", bscnn(24, 36))

print("UCLN(18, 24) =", uscln(18, 24))
print("BSCNN(18, 24) =", bscnn(18, 24))

print("UCLN(7, 13) =", uscln(7, 13))
print("BSCNN(7, 13) =", bscnn(7, 13))


# ===== Gọi thử kiem_tra_nguyen_to với 3 giá trị =====
print("29 có phải số nguyên tố không?", kiem_tra_nguyen_to(29))
print("15 có phải số nguyên tố không?", kiem_tra_nguyen_to(15))
print("2 có phải số nguyên tố không?", kiem_tra_nguyen_to(2))


# ===== Gọi thử kiem_tra_so_hoan_thien với 3 giá trị =====
print("28 có phải số hoàn thiện không?", kiem_tra_so_hoan_thien(28))
print("6 có phải số hoàn thiện không?", kiem_tra_so_hoan_thien(6))
print("12 có phải số hoàn thiện không?", kiem_tra_so_hoan_thien(12))