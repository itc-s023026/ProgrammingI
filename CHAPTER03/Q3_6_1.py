import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sample4 = random.sample(numbers, k=4)
my_list = "".join(sample4)
while True:
    val = input()
    if val == my_list:
        print("OK")
        break
    else:
        print(val, ":NG")
