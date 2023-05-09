# 1. Write a Python program that takes a list of strings as input and outputs the number of times
# each string appears in the list, using a dictionary and conditional statement

fruits = ['mando', 'banana', 'kiwi', 'orange', 'peas']
begin = {}
for string in fruits:
    if string in begin:
        begin[string] += 1
    else:
        begin[string] = 1
for string, begin in begin.items():
    print(string, begin)  


# 2. Write a Python program that takes a list of numbers as input
# and outputs the median of the numbers 

def get_median(nums):
    sorted_num = sorted(nums)
    x = len(sorted_num)
    middle = x //2
    if x % 2 == 0:
        median = (sorted_num[middle-1]+sorted_num[middle])/2
    else:
        median = sorted_num[middle]
        return median
    numbers = [3, 6, 4, 8, 2, 1, 8, 9]
    print(get_median(numbers))


# 3. a Python program that takes a list of numbers as input and outputs the
# second largest number in the list using conditional statements and a for loop.

def def_get_second_largest(number):
    get_1= number[0]
    count_2=number[0]
    for numx in number:
        if numx > get_1:
            count_2 = get_1
            get_1 = numx
        elif numx > count_2 and numx != get_1:
            count_2 = numx
    return count_2
input_list = [5, 7, 9, 1, 3, 9, 10]
answer = def_get_second_largest(input_list)
print(answer)

# 4. Write a Python program that takes a year as input and determines if it is a leap year.

def get_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
input_year = 2023
result = get_leap_year(input_year)
print(result)


# 5. Write a Python program that takes a string as input and checks if it is a palindrome 
# (reads the same forwards and backwards), ignoring spaces and punctuation.


def is_palindrome(string1):
    string1 = "madam"

    return string1 == string1[::-1]


