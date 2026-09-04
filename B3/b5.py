import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

# Yeu cau: Tinh khoang cach cua tung diem trong cac_diem so voi goc toa do (0, 0)
cac_diem = [(0, 0), (3, 4), (6, 8)]

for diem in cac_diem:
    x, y = diem
    kc_goc = math.sqrt(x ** 2 + y ** 2)
    print(f"Khoang cach tu {diem} den goc toa do (0, 0) la: {round(kc_goc, 2)}")