# Bài tập 4.1: Tính giai thừa của số nguyên n bằng vòng lặp while

n = 5
giai_thua = 1
i = 1

while i <= n:
    giai_thua = giai_thua * i
    i += 1

print(f"{n}! = {giai_thua}")