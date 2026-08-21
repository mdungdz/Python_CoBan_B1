# Bài tập 5.1 – Toán tử số học
a = 17
b = 5

print("--- Bài tập 5.1 ---")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)



# Bài tập 5.2 – Toán tử so sánh & logic
diem = 6.5
tuoi = 20
print("\n--- Bài tập 5.2 ---")
la_loai_kha = (diem >= 6.5) and (diem < 8.0)
print("Diểm đạt loại Khá:", la_loai_kha)

dieu_kien_tuoi = (tuoi < 18) or (tuoi > 60)
print("Tuổi < 18 hoặc > 60:", dieu_kien_tuoi)

phu_dinh_tuoi = not dieu_kien_tuoi
print("Phủ định điều kiện tuổi (not):", phu_dinh_tuoi)



# Bài tập 5.3 – Toán tử gán & toán tử đặc biệt
print("\n--- Bài tập 5.3 ---")
x = 10
x += 5
print("x sau += 5 là:", x)
x -= 3
print("x sau -= 3 là:", x)
x *= 2
print("x sau *= 2 là:", x)
x /= 4
print("x sau /= 4 là:", x)
x //= 2
print("x sau //= 2 là:", x)
x **= 3
print("x sau **= 3 là:", x)

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không (in):", 3 in danh_sach)

list1 = [1, 2, 3]
list2 = list1
print("list1 và list2 cùng tham chiếu (is):", list1 is list2)

# Bài tập 5.4 – Độ ưu tiên toán tử
print("\n--- Bài tập 5.4 ---")
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)