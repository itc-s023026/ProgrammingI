def my_numbers(numbers):
    my_numbers = [num**2 for num in numbers]
    return my_numbers


my_list = [1, 2, 3, 4, 5]
result = my_numbers(my_list)
print(result)
