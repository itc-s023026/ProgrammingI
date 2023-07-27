def my_list():
    for i in range(1, 10):
        for j in range(1, 10):
            answer = i * j
            print(f"{i}×{j}={answer}")
            print("\n", end="")


my_list()
