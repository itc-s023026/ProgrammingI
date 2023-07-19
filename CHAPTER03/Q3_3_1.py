my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama"]
s = []
for i in my_list:
    if len(i) >= 6:
        s.append(i)
        print(s)
