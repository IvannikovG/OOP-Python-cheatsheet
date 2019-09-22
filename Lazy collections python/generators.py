# Generators


def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5, 6])
print(my_nums)
#my_nums2 = map(lambda e: e * e, [1, 2, 3, 4, 5, 6])
# standard way of producing a sequence of something is above

# On the other hand we can use generators
# It is actually a lazy way of evaluating the collection


def square_numbers_lazy(nums):
    for i in nums:
        yield (i * i)


my_nums_lazy = square_numbers_lazy([1, 2, 3, 4, 5])
# print(my_nums_lazy)
# print(next(my_nums_lazy))
for num in my_nums_lazy:
    print(num)
# for loop knows when to stop, even though the thing is lazy

my_nums_another = (x * x for x in [1, 2, 3, 4, 5])
print(my_nums_another) #another generator
