name_age = {"tanaka": 35, "satou": 25, "auzuki": 27}


def name(my_list, key):
    try:
        return my_list[key]
    except:
        return "key is not found"


print(name(name_age, "satou"))
print(name(name_age, "yamada"))
