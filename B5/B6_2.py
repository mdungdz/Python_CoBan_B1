# Bài tập 6.2: In hình thoi sao cân đối bằng vòng lặp lồng nhau

n = 4

# Nua tren cua hinh thoi
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Nua duoi cua hinh thoi
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))