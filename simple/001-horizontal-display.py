# Python print function display it content in oneline and ending with new line
# because print function has paramater called 'end'  and by default this parameter has value '\n'

# To display value horizontally espicially when we iterate ove iterable object we can use the foolong code

numbers = [1, 2, 3, 4, 5, 6, 7]

for num in numbers:
    print(num, end="")  # output 1234567

# And print function has paramater called 'sep' to separate its arrgs
# Example

print('02', '05', '2024', sep='/')  # output 02/05/2024
