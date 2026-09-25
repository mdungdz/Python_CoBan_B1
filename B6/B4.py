so_luot_truy_cap = 0  # biến global


def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1


def vi_du_bien_local():
    so_luot_truy_cap = 100  # đây là biến LOCAL, khác với biến global cùng tên
    print("Bên trong hàm, biến local =", so_luot_truy_cap)


tang_luot_truy_cap()
tang_luot_truy_cap()
print("Số lượt truy cập (global):", so_luot_truy_cap)

vi_du_bien_local()
print("Sau khi gọi hàm, biến global vẫn là:", so_luot_truy_cap)