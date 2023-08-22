def my_list(x):
    try:
        return sum(x) / len(x)
    except:
        print("list_length:", len(x))
        return None


print(my_list([3.9, 4.5, 2, 3]))
print(my_list([]))
