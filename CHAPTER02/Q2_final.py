import random

name = "m"

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

while True:
    random_char = random.choice(alphabet)  # 名前からランダムな文字を取得
    print(f"{random_char}")

    if name == random_char:
        break
