for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 奇数だけ表示される


for i in range(10):
    if i % 2 == 0:
        break
    print(i)  # 何も表示されない
