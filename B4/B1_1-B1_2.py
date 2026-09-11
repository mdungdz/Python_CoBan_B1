sinh_vien = {
    "ho_ten": "Nguyen Manh Dung",
    "nam_sinh": 2006,
    "diem_tb": 9.5
}

print(sinh_vien["ho_ten"])            # truy xuat theo khoa
print(sinh_vien.get("diem_tb"))        # truy xuat an toan bang get()
print(sinh_vien.get("lop", "Chua co")) # get() voi gia tri mac dinh neu khong co khoa

sinh_vien["lop"] = "CNTT01"       # them khoa moi
sinh_vien["diem_tb"] = 9.0        # sua gia tri khoa da co
print(sinh_vien)

diem_cu = sinh_vien.pop("diem_tb") # xoa theo khoa, tra ve gia tri vua xoa
print(sinh_vien, "- diem da xoa:", diem_cu)

sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"}) # cap nhat/them nhieu khoa cung luc
print(sinh_vien) 