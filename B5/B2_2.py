# Bài tập 2.2: Tìm số lớn nhất trong 3 số nhập vào từ bàn phím
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
c = float(input("Nhap so thu ba: "))

if a >= b and a >= c:
    lon_nhat = a
elif b >= a and b >= c:
    lon_nhat = b
else:
    lon_nhat = c

print("So lon nhat la:", lon_nhat)