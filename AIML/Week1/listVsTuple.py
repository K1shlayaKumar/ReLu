my_list = [10, 20, 30, 40]
my_tuple = (10, 20, 30, 40)

my_list[1] = 99
print("List after modification:", my_list)

my_tuple[1] = 99
# The line above won't even get compiled because Tuples are immutable as in you can't modify the values
