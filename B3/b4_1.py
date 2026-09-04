# --- BÀI TẬP 4.1: Khai báo & tính bất biến ---
toa_do = (3, 5)
print(toa_do, type(toa_do))

# Dòng gây lỗi cố tình của đề bài, nhớ thêm dấu # ở đầu để chương trình chạy tiếp:
# toa_do[0] = 10


# --- BÀI TẬP 4.2: Unpacking tuple ---
x, y = toa_do
print("x =", x, "va y =", y)

# Doi gia tri 2 bien bang unpacking (khong can bien tam)
a, b = 10, 20
a, b = b, a
print("a =", a, "va b =", b)


# --- BÀI TẬP 4.3: Trả về nhiều giá trị từ một biểu thức ---
c, d = 17, 5
thuong_du = divmod(c, d)     # divmod tra ve mot tuple (thuong, du)
thuong, du = thuong_du       # unpacking ket qua
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")