def sort_by(num1, num2):
    print("{}:{}".format(num1, num2))
    return -1
import functools
a = [7,6,5,3,4]

print(sorted(a, key=functools.cmp_to_key(sort_by)))