# Bài tập 6.1: In hình tam giác sao bằng vòng lặp lồng nhau

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()