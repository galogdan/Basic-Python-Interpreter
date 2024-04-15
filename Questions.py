# This file is for part B of the project questions 9-14


from functools import reduce


################Question 9######################
print("################Question 9######################")
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)
print(factorial(5))


################Question 10######################
print("################Question 10######################")
concatenate_with_space = lambda strings: reduce(lambda x, y: x + ' ' + y, strings)
strings = ['check', 'if', 'its', 'working']
single_string = concatenate_with_space(strings)
print(single_string)

################Question 11######################
print("################Question 11######################")
def cumulative_sum_of_squares_even_numbers(lists):
    return list(map(
        lambda sublist: reduce(
            lambda total, num: total + (
                lambda even: (
                    lambda square: (
                        lambda add_square: add_square(num)
                    )(lambda n: square(n) if even(n) else 0)
                )(lambda n: n ** 2)
            )(lambda n: n % 2 == 0),
            sublist,
            0
        ),
        lists
    ))


lists_of_numbers_to_square = [
    [2, 4, 6, 5, 8],
    [1, 5, 10, 9],
    [8, 11, 12, 4]
]

calculated_square_lists = cumulative_sum_of_squares_even_numbers(lists_of_numbers_to_square)
print(calculated_square_lists)


###############Question 12#######################
print("################Question 12######################")
nums = [1, 2, 3, 4, 5, 6]
sum_squared = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(sum_squared)


##############Question 13#######################
print("################Question 13######################")

count_palindromes = lambda lists: list(map(lambda sublist: reduce(lambda count, string: count + 1 if string == string[::-1] else count, sublist, 0), lists))

# Example usage
lists_of_strings = [
    ["racecar", "level", "hello", "madam"],
    ["world", "noon", "deed", "test"],
    ["python", "civic", "radar", "tree", "aca"]
]

num_of_palindroms = count_palindromes(lists_of_strings)
print(num_of_palindroms)


##############Question 14#######################
print("################Question 14######################\nWritten below")
"""

In this program we can see the differences between lazy and eager evaluation.
While in the eager evaluation all the values generated and only after performing squared_values = [square(x) for x in values],
in the lazy evaluation the calculations occuring exactly when needed as we can see we perform square for each generated instead of generating all first.
In that way the "lazy evaluation" delaying calculate the evaluations until needed. 

"""
